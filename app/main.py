from fastapi import FastAPI
from app.core.config import Settings, settings as default_settings
from app.core.logging import setup_logging
from app.api.health import router as health_router
from app.api.upload import router as upload_router


def create_app(settings: Settings = default_settings) -> FastAPI:
    setup_logging()

    app = FastAPI(title=settings.app_name)

    app.include_router(health_router)
    app.include_router(upload_router)
    app.state.settings = settings
    return app


app = create_app()
