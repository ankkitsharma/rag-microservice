from fastapi.testclient import TestClient
from app.main import app


def test_rejects_non_text_file():
    client = TestClient(app)

    response = client.post(
        "/upload",
        files={"file": ("evil.exe", b"fake-binary", "application/octet-stream")},
    )

    assert response.status_code == 400


def test_rejects_large_file():
    client = TestClient(app)

    big_content = b"a" * (2 * 1024 * 1024 + 1)

    response = client.post(
        "/upload", files={"file": ("big.txt", big_content, "text/plain")}
    )

    assert response.status_code == 413


def test_accepts_valid_text_file():
    client = TestClient(app)

    response = client.post(
        "/upload", files={"file": ("doc.txt", b"Hello world", "text/plain")}
    )

    assert response.status_code == 200
    assert "upload_id" in response.json()
