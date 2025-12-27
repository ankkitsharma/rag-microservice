def test_app_starts_without_error():
    from app.main import create_app

    app = create_app()
    assert app is not None
