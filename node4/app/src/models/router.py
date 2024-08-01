from fastapi import APIRouter
from models.schemas import IrisRequest, IrisResponse
import joblib
import numpy as np
from sklearn import datasets

router = APIRouter()

# Load model from file
model = joblib.load('./models/artifacts/model.pkl')

# Load iris dataset to get target names
iris = datasets.load_iris()

@router.post("/predict", response_model=IrisResponse)
async def predict_iris(data: IrisRequest):
    input_data = np.array([[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]])
    prediction = model.predict(input_data)
    predicted_class = iris.target_names[prediction[0]]
    return IrisResponse(predicted_class=predicted_class)