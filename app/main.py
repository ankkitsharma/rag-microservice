from fastapi import FastAPI
from app.api.health import router as health_router
from app.core.config import Settings, settings as default_settings
from app.core.logging import setup_logging


def create_app(settings: Settings = default_settings) -> FastAPI:
    setup_logging()

    app = FastAPI(title=settings.app_name)

    app.include_router(health_router)
    app.state.settings = settings
    return app


app = create_app()
