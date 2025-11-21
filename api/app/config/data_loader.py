"""
Data loader for initial data seeding
"""
from sqlalchemy.orm import Session
from api.app.database import SessionLocal
from api.app.models.painting import Painting
from api.app.repositories.painting_repository import PaintingRepository


def init_data():
    """
    Initialize database with sample data if empty
    """
    db: Session = SessionLocal()
    try:
        repository = PaintingRepository(db)
        
        # Only load data if database is empty
        if repository.count() == 0:
            painting1 = Painting(
                code="painting_01",
                title="The Mona Lisa",
                author="Leonardo da Vinci",
                description="Portrait of Lisa Gherardini, known as La Gioconda.",
                image_url="https://upload.wikimedia.org/wikipedia/commons/6/6a/Mona_Lisa.jpg",
                type="image"
            )
            
            painting2 = Painting(
                code="painting_02",
                title="Las Meninas",
                author="Diego Velázquez",
                description="Baroque painting representing the Infanta Margarita and her entourage.",
                image_url="https://upload.wikimedia.org/wikipedia/commons/6/6f/Las_Meninas_01.jpg",
                type="image"
            )
            
            repository.save(painting1)
            repository.save(painting2)
            print("Initial paintings loaded successfully")
    except Exception as e:
        print(f"Error loading initial data: {e}")
    finally:
        db.close()
