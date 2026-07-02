from fastapi import FastAPI
from app.core.config import settings
from app.api.health import router as health_router


app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG
)


app.include_router(health_router)


@app.get("/")
async def root():
    return {"message": settings.APP_NAME}