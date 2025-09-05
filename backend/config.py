# backend/config.py
# Arquivo de configuração para o projeto

from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    """
    Configurações da aplicação
    """
    # BASE URL do serviço (dev/prod)
    base_url: str = "http://127.0.0.1:8000"
    # MongoDB Atlas - official connection string
    mongodb_url: str = "mongodb+srv://luiz_test_encurtador:a6UXnqk9LoVVh6dt@cluster0.cdebnt2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    database_name: str = "url_shortener"
    
    # API Settings
    debug: bool = True
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    
    class Config:
        env_file = ".env"

# Instância global das configurações
settings = Settings()
