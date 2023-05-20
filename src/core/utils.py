from pathlib import Path

import aiofiles
from fastapi import UploadFile

from .config import BASE_DIR, settings


async def save_media_file(file: UploadFile, directory: str | Path = ''):
    """Save a media file to a directory."""

    file_path = Path(settings.MEDIA_ROOT) / directory / file.filename
    file_path.parent.mkdir(parents=True, exist_ok=True)
    contents = await file.read()
    async with aiofiles.open(file_path, "wb") as f:
        await f.write(contents)
    return str(file_path.relative_to(BASE_DIR))