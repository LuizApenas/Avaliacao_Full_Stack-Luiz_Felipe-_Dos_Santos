# backend/models.py
# Modelos de dados usando Beanie (MongoDB ODM)

from beanie import Document
from pydantic import Field, HttpUrl
from datetime import datetime
from typing import Optional

class URL(Document):
    """
    Modelo para URLs encurtadas
    """
    original_url: HttpUrl = Field(..., description="URL original a ser encurtada")
    short_id: str = Field(..., unique=True, index=True, description="Identificador único da URL")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Data de criação")
    is_active: bool = Field(default=True, description="Se a URL está ativa")
    failed_checks: int = Field(default=0, description="Número de verificações de saúde falhadas")
    last_check: Optional[datetime] = Field(default=None, description="Última verificação de saúde")
    short_url: Optional[HttpUrl] = None
    class Settings:
        name = "urls"  # Nome da coleção no MongoDB
        indexes = [
            "short_id",  # Índice para busca rápida
            "created_at",
            "is_active"
        ]

class URLMetric(Document):
    """
    Modelo para métricas de acesso às URLs
    """
    short_id: str = Field(..., index=True, description="ID da URL acessada")
    accessed_at: datetime = Field(default_factory=datetime.utcnow, description="Data/hora do acesso")
    user_agent: Optional[str] = Field(default=None, description="User agent do navegador")
    ip_address: Optional[str] = Field(default=None, description="Endereço IP do visitante")
    referer: Optional[str] = Field(default=None, description="Site de origem do acesso")
    
    class Settings:
        name = "url_metrics"  # Nome da coleção no MongoDB
        indexes = [
            "short_id",  # Índice para busca rápida por URL
            "accessed_at",  # Índice para consultas por data
            [("short_id", 1), ("accessed_at", -1)]  # Índice composto
        ]
