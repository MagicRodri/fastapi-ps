from pathlib import Path
from fastapi import UploadFile
from pydub import AudioSegment
from .config import BASE_DIR, settings


def save_media_file(file: UploadFile, directory: str | Path = ''):
    """Save a media file to a directory."""

    file_path = Path(settings.MEDIA_ROOT) / directory / file.filename
    file_path.parent.mkdir(parents=True, exist_ok=True)
    contents = file.read()
    with open(file_path, "wb") as f:
        f.write(contents)
    return str(file_path.relative_to(BASE_DIR))

def save_wav_to_mp3(file: UploadFile, directory:str|Path = ''):
    """ Convert uploaded wav file to mp3 """
    file_path = Path(settings.MEDIA_ROOT) / directory / file.filename
    file_path = file_path.with_suffix('.mp3') # same filename with mp3 extension
    file_path.parent.mkdir(parents=True, exist_ok=True)
    wav_audio = AudioSegment.from_file(file.file,format='wav')
    _ = wav_audio.export(str(file_path),format='mp3')
    return str(file_path.relative_to(BASE_DIR))