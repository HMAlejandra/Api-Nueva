"""
Artwork model - represents a general artwork entity
"""
from sqlalchemy import Column, Integer, String
from api.app.database import Base


class Artwork(Base):
    __tablename__ = "artwork"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    code = Column(String, nullable=True)
    title = Column(String, nullable=True)
    author = Column(String, nullable=True)
    description = Column(String, nullable=True)
    image_url = Column(String, nullable=True)
    type = Column(String, nullable=True)

    def __repr__(self) -> str:
        return f"<Artwork(id={self.id}, title='{self.title}')>"

