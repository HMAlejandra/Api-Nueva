"""
Data loader for initial data seeding
"""
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.artwork import Artwork
from app.repositories.artwork_repository import ArtworkRepository


def init_data():
    """
    Initialize database with sample data if empty
    """
    db: Session = SessionLocal()
    try:
        repository = ArtworkRepository(db)
        
        # Only load data if database is empty
        if repository.count() == 0:
            artwork1 = Artwork(
                code="artwork_01",
                title="The Mona Lisa",
                author="Leonardo da Vinci",
                description="Portrait of Lisa Gherardini, better known as Mona Lisa.",
                image_url="https://upload.wikimedia.org/wikipedia/commons/6/6a/Mona_Lisa.jpg",
                type="image"
            )
            
            artwork2 = Artwork(
                code="artwork_02",
                title="Las Meninas",
                author="Diego Velázquez",
                description="Baroque painting showing the Infanta Margarita surrounded by her entourage.",
                image_url="https://upload.wikimedia.org/wikipedia/commons/6/6f/Las_Meninas_01.jpg",
                type="image"
            )
            
            repository.save(artwork1)
            repository.save(artwork2)
            print("Initial data loaded successfully")
    except Exception as e:
        print(f"Error loading initial data: {e}")
    finally:
        db.close()

