from api.app.database import Base, engine

print("📌 Creating database tables...")
Base.metadata.create_all(bind=engine)
print("✅ Tables created successfully!")