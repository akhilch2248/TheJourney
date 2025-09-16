from jose import jwt  # same lib we use in auth routes
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

# 1) Config from .env
APP_SECRET = os.getenv("APP_SECRET", "dev-only-weak-secret")  # never use default in prod
ALGORITHM = "HS256"
DEFAULT_EXPIRE_MIN = int(os.getenv("TOKEN_EXPIRE_MINUTES", "60"))

def create_access_token(claims: dict, expires_minutes: int | None = None) -> str:
    """
    Create a signed JWT containing our claims.
    - claims: dict, e.g. {"sub": "123"} where 'sub' = user id
    - expires_minutes: override expiry if needed
    """
    to_encode = claims.copy()
    exp = datetime.utcnow() + timedelta(minutes=expires_minutes or DEFAULT_EXPIRE_MIN)
    to_encode.update({"exp": exp})
    return jwt.encode(to_encode, APP_SECRET, algorithm=ALGORITHM)

def decode_access_token(token: str) -> dict:
    """
    Verify & decode our app JWT. Raises if token invalid/expired.
    """
    return jwt.decode(token, APP_SECRET, algorithms=[ALGORITHM])

