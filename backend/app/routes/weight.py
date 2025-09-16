from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models.weight import WeightLog
from ..schemas.weight import WeightCreate, WeightRead

# ✅ NEW: imports for auth
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from ..utils.auth_tokens import APP_SECRET, ALGORITHM
from ..models.user import User

router = APIRouter(prefix="/weights", tags=["weights"])


# ----------------------
# DB dependency
# ----------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ----------------------
# ✅ NEW: Helper to extract user from token
# ----------------------
#oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/apple")  # "tokenUrl" is just for docs

from fastapi.security import HTTPBearer
from fastapi.security import HTTPAuthorizationCredentials

oauth2_scheme = HTTPBearer()

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
):
    """
    1) Read bearer token from Authorization header.
    2) Decode & verify it using APP_SECRET.
    3) Load the user from DB.
    """
    token = credentials.credentials
    try:
        payload = jwt.decode(token, APP_SECRET, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token: missing subject")
        user = db.query(User).filter(User.id == int(user_id)).first()
        if user is None:
            raise HTTPException(status_code=401, detail="User not found")
        return user
    except JWTError:
        raise HTTPException(status_code=401, detail="Token invalid or expired")


# ----------------------
# Routes (auth enforced now)
# ----------------------
@router.post("/", response_model=WeightRead, status_code=201)
def create_weight(
    payload: WeightCreate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),   # ✅ enforces login
):
    record = WeightLog(
        date=payload.date,
        weight_kg=payload.weight_kg,
        source=payload.source or "manual",
        user_id=user.id
    )
    db.add(record)
    db.commit()
    db.refresh(record)
    return record


@router.get("/", response_model=List[WeightRead])
def list_weights(
    source: Optional[str] = None,
    limit: int = 50,
    offset: int = 0,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),   # ✅ enforces login
):
    query = db.query(WeightLog).filter(WeightLog.user_id == user.id)
    if source:
        query = query.filter(WeightLog.source == source)
    return query.order_by(WeightLog.date.desc()).offset(offset).limit(limit).all()
