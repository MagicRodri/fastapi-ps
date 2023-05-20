import uuid
from pathlib import Path

from db.base import Base
from sqlalchemy import UUID, Boolean, Column, ForeignKey, Integer, String


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    access_token = Column(UUID, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)


class Record(Base):
    id = Column(UUID, primary_key=True, index=True, default=uuid.uuid4)
    user = Column(Integer, ForeignKey('user.id'))
    file = Column(String, index=True)

    @property
    def filename(self):
        return Path(self.file).name