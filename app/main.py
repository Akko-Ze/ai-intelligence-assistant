from fastapi import FastAPI
from app.core.config import settings
from app.api.health import router as health_router
from app.api.chat import router as chat_router
import logging
from app.utils.logger import setup_logger


setup_logger()

logger = logging.getLogger(__name__)


app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG
)

logger.info("AI Intelligence Assistant started.")


app.include_router(health_router)
app.include_router(chat_router)


@app.get("/")
async def root():
    return {"message": settings.APP_NAME}