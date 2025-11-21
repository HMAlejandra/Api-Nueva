"""
Painting model - represents a painting entity in the museum system
"""
from sqlalchemy import Column, Integer, String
from app.database import Base


class Painting(Base):
    __tablename__ = "painting"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    code = Column(String, nullable=True)
    title = Column(String, nullable=True)
    artist = Column(String, nullable=True)
    description = Column(String, nullable=True)
    image_url = Column(String, nullable=True)
    category = Column(String, nullable=True)

    def __repr__(self) -> str:
        return f"<Painting(id={self.id}, title='{self.title}')>"

