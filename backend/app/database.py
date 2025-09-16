from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# 1. Load environment variables from .env
load_dotenv()

# 2. Read DATABASE_URL from .env
DATABASE_URL = os.getenv("DATABASE_URL")

# 2.1 Debug: print to confirm
print("DATABASE_URL loaded:", DATABASE_URL)

# 3. Create engine (connection to Postgres)
engine = create_engine(DATABASE_URL)

# 4. Session maker (each request gets a DB session)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 5. Base class for ORM models
Base = declarative_base()

