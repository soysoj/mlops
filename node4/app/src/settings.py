from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    model_path: str = "./models/artifacts/model.pkl"
    server_host: str = "0.0.0.0"
    server_port: int = 8000

    class Config:
        protected_namespaces = ("settings_",)
        env_file = ".env" # 보이지 않는 파일


settings = Settings()
