import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Reads DATABASE_URL from environment (set automatically by Railway PostgreSQL plugin)
# Falls back to local for development
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:#Hari012345@localhost:5432/carbon_mrv"
)

# Railway provides URLs starting with "postgres://" — SQLAlchemy needs "postgresql://"
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
