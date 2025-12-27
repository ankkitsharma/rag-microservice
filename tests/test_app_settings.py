from app.main import create_app
from app.core.config import Settings


def test_app_users_custom_settings():
    test_settings = Settings(
        app_name="Test RAG",
        environment="test",
    )

    app = create_app(settings=test_settings)

    assert app.title == "Test RAG"
    assert app.state.settings.environment == "test"
