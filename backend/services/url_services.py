from typing import Optional, List
from urllib.parse import urlparse
from config import settings
from models import URL
from utils import generate_short_id

ID_LENGTH = 6
MAX_ATTEMPTS = 10


def validar_url(original_url: str) -> bool:
    #Valida se a URL é válida
    if not original_url or not original_url.startswith(("http://","https://")):
        return False
    parsed = urlparse(original_url.strip())
    return bool(parsed.scheme and parsed.netloc)

def normalizar_url(original_url: str) -> str:
    #Normaliza a URL removendo espaços extras 
    return original_url.strip()

async def gerar_short_id_unico(length: int = ID_LENGTH, max_attempts: int = MAX_ATTEMPTS) -> str:
    #Gera um ID encurtado único para a URL encurtada na base de dados
    for _ in range(max_attempts):
        candidate = generate_short_id(length)  
        exist = await URL.find_one((URL.short_id == candidate))
        if not exist:
            return candidate
    raise ValueError("Não foi possível gerar um ID encurtado único")

async def criar_url_encurtada(original_url: str) -> URL:
    # Create and persist a shortened URL
    url = normalizar_url(original_url)
    if not validar_url(url):
        raise ValueError("A URL original é inválida")

    short_id = await gerar_short_id_unico()
    short_url = f"{settings.base_url.rstrip('/')}/{short_id}"

    doc = URL(
        original_url=url,
        short_id=short_id,
        short_url=short_url,
    )
    await doc.insert()
    return doc

async def buscar_url_por_short_id(short_id: str) -> Optional[URL]:
    #Busca o doc com a url encurtada
    return await URL.find_one((URL.short_id == short_id))

async def listar_urls(skip: int = 0, limit: int = 100, somente_ativas: bool = False) -> List[URL]:
    query = URL.find(URL.is_active == True) if somente_ativas else URL.find_all()
    # ordena por mais recentes
    return await query.sort("-created_at").skip(skip).limit(limit).to_list()