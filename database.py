from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# URL de connexion PostgreSQL
DATABASE_URL = "postgresql://postgres:root@localhost:5432/product_db"

# Création du moteur de connexion
engine = create_engine(DATABASE_URL)

# Création de la session
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

# Base pour créer les modèles
Base = declarative_base()
