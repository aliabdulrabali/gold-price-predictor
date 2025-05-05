from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
DATABASE_URL = os.environ.get("postgresql://gold_db_8919_user:44Zhduf6vDSxLmcVJ6fEcgh4QbXNNPKL@dpg-d0c9vupr0fns73e77bmg-a/gold_db_8919")

DATABASE_URL = "postgresql://alialyafai:weemo@localhost/sawapay_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
