from fastapi import FastAPI
from models.router import router as model_router
import uvicorn
from settings import settings
app = FastAPI()

app.include_router(model_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.server_host, port=settings.server_port)