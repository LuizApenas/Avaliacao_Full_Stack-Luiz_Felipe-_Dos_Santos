# backend/database.py
# Configuração da conexão com MongoDB usando Beanie

import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi
from beanie import init_beanie
from config import settings

# Modelos que serão criados depois
from models import URL, URLMetric

class Database:
    client: AsyncIOMotorClient = None
    database = None

# Instância global do banco
db = Database()

async def connect_to_mongo():
    """
    Conectar ao MongoDB Atlas usando ServerApi oficial
    """
    try:
        print("🔌 Conectando ao MongoDB Atlas...")
        
        # Criar cliente MongoDB usando ServerApi como no exemplo oficial
        db.client = AsyncIOMotorClient(
            settings.mongodb_url,
            server_api=ServerApi('1'),
            serverSelectionTimeoutMS=30000,
            connectTimeoutMS=30000,
            socketTimeoutMS=30000
        )
        
        # Selecionar database
        db.database = db.client[settings.database_name]
        
        # Testar conexão
        await db.client.admin.command('ping')
        print("✅ Pinged your deployment. You successfully connected to MongoDB!")
        
        # Inicializar Beanie com os modelos
        await init_beanie(
            database=db.database,
            document_models=[URL, URLMetric]  # Modelos que criaremos
        )
        print("✅ Beanie inicializado com sucesso!")
        
    except Exception as e:
        print(f"❌ Erro ao conectar com MongoDB: {e}")
        raise

async def close_mongo_connection():
    """
    Fechar conexão com MongoDB
    """
    if db.client:
        db.client.close()
        print("🔌 Conexão com MongoDB fechada")

async def test_connection():
    """
    Testar conexão com MongoDB
    """
    try:
        await db.client.admin.command('ping')
        return True
    except Exception as e:
        print(f"❌ Erro no teste de conexão: {e}")
        return False
