``` mermaid
graph TD;
    A[Database: MySQL] --> B[Train Model: PyTorch, TensorFlow, W&B];
    B --> C[Save Model: PyTorch, TensorFlow, W&B];
    C --> D[Model Registry: mlFlow];
    D --> E[Model Deployment: FastAPI];
    E --> F[Stream Serving: FastAPI];

    A -.-> G[Data Pipeline : X];
    G -.-> F;

    subgraph Model_Development;
        B;
        C;
    end;

    subgraph Model_Deployment;
        E;
        F;
    end;
```
