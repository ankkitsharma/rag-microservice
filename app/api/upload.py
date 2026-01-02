from fastapi import APIRouter, UploadFile, File, HTTPException
import uuid
from pathlib import Path

router = APIRouter()

MAX_FILE_SIZE = 2 * 1024 * 1024  # 2MB
ALLOWED_TYPES = {"text/plain", "text/markdown"}
UPLOAD_DIR = Path("app/storage")

UPLOAD_DIR.mkdir(exist_ok=True)


@router.post("/upload")
async def upload(file: UploadFile = File(...)):
    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(status_code=400, detail="Unsupported file type")

    upload_id = str(uuid.uuid4())
    file_path = UPLOAD_DIR / f"{upload_id}.txt"

    size = 0

    with open(file_path, "wb") as out:
        while True:
            chunk = await file.read(1024)
            if not chunk:
                break

            size += len(chunk)
            if size > MAX_FILE_SIZE:
                out.close()
                file_path.unlink(missing_ok=True)
                raise HTTPException(status_code=413, detail="File too large")

            out.write(chunk)

    return {
        "upload_id": upload_id,
        "size": size,
    }
