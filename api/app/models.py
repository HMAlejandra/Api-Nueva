from sqlalchemy import Column, Integer, String, Text
from .database import Base

class Painting(Base):
    __tablename__ = "painting"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    image_url = Column(Text, nullable=False)