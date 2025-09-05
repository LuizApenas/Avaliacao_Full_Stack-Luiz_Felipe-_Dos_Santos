# backend/main.py
# App FastAPI mínimo com startup/shutdown e redirect

from fastapi import FastAPI, HTTPException, Request
from starlette.responses import RedirectResponse
from router import urls
from database import connect_to_mongo, close_mongo_connection
from services.url_services import buscar_url_por_short_id
from fastapi.middleware.cors import CORSMiddleware
from config import settings
import asyncio
import uvicorn
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi
from models import URLMetric


app = FastAPI(title="URL Shortener")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.on_event("startup")
async def on_startup():
    await connect_to_mongo()

@app.on_event("shutdown")
async def on_shutdown():
    await close_mongo_connection()

# Endpoints de API
app.include_router(urls.router, prefix="/api", tags=["urls"])

@app.get("/{short_id}")
async def redirect(short_id: str, request: Request):
    doc = await buscar_url_por_short_id(short_id)
    if not doc:
        raise HTTPException(status_code=404, detail="Short ID não encontrado")
    if not doc.is_active:
        raise HTTPException(status_code=410, detail="URL desativada")

    try:
        metric = URLMetric(
            short_id=doc.short_id,
            user_agent=request.headers.get("user-agent"),
            ip_address=(request.client.host if request.client else None),
            referer=request.headers.get("referer"),
        )
        await metric.insert()
    except Exception as e:
        print(f"⚠️ Failed to record metric: {e}")

    return RedirectResponse(url=str(doc.original_url), status_code=301)


# Preflight database check before starting the server when running as script
async def _preflight_database_check() -> None:
    try:
        print("🔎 Running database preflight check...")
        # Use same configuration as the official MongoDB Atlas example
        client = AsyncIOMotorClient(
            settings.mongodb_url,
            server_api=ServerApi('1'),
            serverSelectionTimeoutMS=30000,
            connectTimeoutMS=30000,
            socketTimeoutMS=30000
        )
        await client.admin.command("ping")
        client.close()
        print("✅ Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as exc:
        print(f"❌ Database preflight failed: {exc}")
        raise


if __name__ == "__main__":
    # Run preflight check and then start the ASGI server
    asyncio.run(_preflight_database_check())
    uvicorn.run(
        app,
        host=settings.api_host,
        port=settings.api_port,
        reload=False,
    )