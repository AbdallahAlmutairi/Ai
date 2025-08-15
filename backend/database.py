"""Database connection utilities."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///trading_bot.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def get_db():
    """Yield a database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
