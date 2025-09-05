from fastapi import APIRouter, HTTPException, Query, Request
from pydantic import HttpUrl, BaseModel
from services.url_services import criar_url_encurtada, listar_urls, buscar_url_por_short_id
from config import settings
from datetime import datetime, timedelta
from models import URL, URLMetric
from contextlib import asynccontextmanager
from fastapi import FastAPI

router = APIRouter()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    # await connect_to_mongo() # This line is removed as per the edit hint
    try:
        yield
    finally:
        # Shutdown
        # await close_mongo_connection() # This line is removed as per the edit hint
        pass # Added pass to avoid syntax error if block is empty

class URLIn(BaseModel):
    # Entrada: validação e normalização de url original
    original_url: HttpUrl

@router.post("/urls")
async def create_short_url(body: URLIn):

    try:
        doc = await criar_url_encurtada(str(body.original_url))
        return {
        "short_id": doc.short_id,
        "original_url": doc.original_url,
       "created_at": doc.created_at,
       "short_url": f"{settings.base_url.rstrip('/')}/{doc.short_id}"
    }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/urls")
async def get_urls(skip: int = Query(0, ge=0), limit: int = Query(50, ge=1, le=200), active: bool = False):
    docs = await listar_urls(skip=skip, limit=limit, somente_ativas=active)
    # compact response
    return [
        {
            "short_id": d.short_id,
            "original_url": str(d.original_url),
            "created_at": d.created_at,
            "is_active": d.is_active,
            "failed_checks": d.failed_checks,
            "short_url": f"{settings.base_url.rstrip('/')}/{d.short_id}"
        }
        for d in docs
    ]
@router.get("/metrics")
async def get_metrics(short_id: str | None = None):
    """
    Return aggregated metrics per short_id: last_hour, last_day, last_month.
    If short_id is provided, return only for that id; otherwise return for all.
    """
    now = datetime.utcnow()
    hour_ago = now - timedelta(hours=1)
    day_ago = now - timedelta(days=1)
    month_ago = now - timedelta(days=30)

    if short_id:
        ids = [short_id]
    else:
        # CORREÇÃO: Busca todas as URLs ordenadas por data de criação (mais recente primeiro)
        docs = await URL.find_all().sort("-created_at").to_list()
        ids = [d.short_id for d in docs]

    results = []
    for sid in ids:
        last_hour = await URLMetric.find(URLMetric.short_id == sid, URLMetric.accessed_at >= hour_ago).count()
        last_day = await URLMetric.find(URLMetric.short_id == sid, URLMetric.accessed_at >= day_ago).count()
        last_month = await URLMetric.find(URLMetric.short_id == sid, URLMetric.accessed_at >= month_ago).count()
        results.append({
            "short_id": sid,
            "last_hour": last_hour,
            "last_day": last_day,
            "last_month": last_month,
        })
    return results

@router.post("/metrics/{short_id}")
async def record_metric(short_id: str, request: Request):
    """
    Record a metric when user clicks on open button without doing redirect.
    This allows tracking clicks in real-time without page refresh.
    """
    try:
        # Verify that the short_id exists and is active
        doc = await buscar_url_por_short_id(short_id)
        if not doc:
            raise HTTPException(status_code=404, detail="Short ID não encontrado")
        if not doc.is_active:
            raise HTTPException(status_code=410, detail="URL desativada")

        # Create and save the metric
        metric = URLMetric(
            short_id=doc.short_id,
            user_agent=request.headers.get("user-agent"),
            ip_address=(request.client.host if request.client else None),
            referer=request.headers.get("referer"),
        )
        await metric.insert()
        
        return {
            "success": True,
            "message": "Métrica registrada com sucesso",
            "original_url": str(doc.original_url)
        }
    except HTTPException:
        raise
    except Exception as e:
        print(f"⚠️ Failed to record metric: {e}")
        raise HTTPException(status_code=500, detail="Erro interno ao registrar métrica")