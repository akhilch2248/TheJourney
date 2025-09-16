#from ..utils.auth_tokens import create_access_token
#from fastapi import APIRouter, HTTPException, Depends
#from sqlalchemy.orm import Session
#from ..database import SessionLocal
#from ..models.user import User
#from ..schemas.user import UserRead
#from jose import jwt   # from python-jose
#import httpx
#
#router = APIRouter(prefix="/auth", tags=["auth"])
#
## ----------------------
## DB dependency
## ----------------------
#def get_db():
#    db = SessionLocal()
#    try:
#        yield db
#    finally:
#        db.close()
#
#
## ----------------------
## Apple Sign-In
## ----------------------
#APPLE_KEYS_URL = "https://appleid.apple.com/auth/keys"
#APPLE_AUDIENCE = "com.yourbundleid.TheJourney"  # TODO: replace with your iOS bundle ID
#
#@router.post("/apple")
#async def auth_with_apple(id_token: str, db: Session = Depends(get_db)):
#    try:
#        # 1️⃣ Fetch Apple public keys
#        async with httpx.AsyncClient() as client:
#            keys = (await client.get(APPLE_KEYS_URL)).json()["keys"]
#
#        decoded = None
#        for key in keys:
#            try:
#                # 2️⃣ Verify the Apple token
#                decoded = jwt.decode(
#                    id_token,
#                    key,
#                    algorithms=["RS256"],
#                    audience=APPLE_AUDIENCE,
#                    issuer="https://appleid.apple.com"
#                )
#                break
#            except Exception:
#                continue
#
#        if not decoded:
#            raise HTTPException(status_code=401, detail="Invalid Apple ID token")
#
#        provider_id = decoded["sub"]
#        email = decoded.get("email")
#
#        # 3️⃣ Check or create user
#        user = db.query(User).filter(
#            User.provider == "apple",
#            User.provider_id == provider_id
#        ).first()
#
#        if not user:
#            user = User(provider="apple", provider_id=provider_id, email=email)
#            db.add(user)
#            db.commit()
#            db.refresh(user)
#
#        # ✅ 4️⃣ NEW: Return app’s session token instead of raw user
#        access_token = create_access_token({"sub": str(user.id)})
#        return {"access_token": access_token, "token_type": "bearer"}
#
#    except Exception as e:
#        raise HTTPException(status_code=401, detail=f"Apple auth failed: {str(e)}")
#
#
## ----------------------
## Google Sign-In
## ----------------------
#GOOGLE_KEYS_URL = "https://www.googleapis.com/oauth2/v3/certs"
#GOOGLE_AUDIENCE = "your-client-id.apps.googleusercontent.com"  # TODO: replace with real Google Client ID
#
#@router.post("/google")
#async def auth_with_google(id_token: str, db: Session = Depends(get_db)):
#    try:
#        # 1️⃣ Fetch Google public keys
#        async with httpx.AsyncClient() as client:
#            keys = (await client.get(GOOGLE_KEYS_URL)).json()["keys"]
#
#        decoded = None
#        for key in keys:
#            try:
#                # 2️⃣ Verify Google token
#                decoded = jwt.decode(
#                    id_token,
#                    key,
#                    algorithms=["RS256"],
#                    audience=GOOGLE_AUDIENCE,
#                    issuer="https://accounts.google.com"
#                )
#                break
#            except Exception:
#                continue
#
#        if not decoded:
#            raise HTTPException(status_code=401, detail="Invalid Google ID token")
#
#        provider_id = decoded["sub"]
#        email = decoded.get("email")
#
#        # 3️⃣ Check or create user
#        user = db.query(User).filter(
#            User.provider == "google",
#            User.provider_id == provider_id
#        ).first()
#
#        if not user:
#            user = User(provider="google", provider_id=provider_id, email=email)
#            db.add(user)
#            db.commit()
#            db.refresh(user)
#
#        # ✅ 4️⃣ NEW: Return app’s session token instead of raw user
#        access_token = create_access_token({"sub": str(user.id)})
#        return {"access_token": access_token, "token_type": "bearer"}
#
#    except Exception as e:
#        raise HTTPException(status_code=401, detail=f"Google auth failed: {str(e)}")





























#############################################################################
#############################################################################
#############################################################################
#######################################################################################################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################
                            #DEVMODE
#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################




from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models.user import User

# ✅ Import our app’s token creator
from ..utils.auth_tokens import create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])


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
# Apple Sign-In (DEV MODE)
# ----------------------
@router.post("/apple")
async def auth_with_apple(id_token: str, db: Session = Depends(get_db)):
    try:
        # 🚧 DEV MODE: instead of verifying with Apple,
        # just treat the id_token string as unique user id
        decoded = {
            "sub": id_token,
            "email": f"{id_token}@test.com"
        }

        provider_id = decoded["sub"]
        email = decoded.get("email")

        # Check if user exists, else create
        user = db.query(User).filter(
            User.provider == "apple",
            User.provider_id == provider_id
        ).first()

        if not user:
            user = User(provider="apple", provider_id=provider_id, email=email)
            db.add(user)
            db.commit()
            db.refresh(user)

        # ✅ Return app session token
        access_token = create_access_token({"sub": str(user.id)})
        return {"access_token": access_token, "token_type": "bearer"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Apple auth failed: {str(e)}")


# ----------------------
# Google Sign-In (DEV MODE)
# ----------------------
@router.post("/google")
async def auth_with_google(id_token: str, db: Session = Depends(get_db)):
    try:
        # 🚧 DEV MODE: instead of verifying with Google,
        # just treat the id_token string as unique user id
        decoded = {
            "sub": id_token,
            "email": f"{id_token}@test.com"
        }

        provider_id = decoded["sub"]
        email = decoded.get("email")

        # Check if user exists, else create
        user = db.query(User).filter(
            User.provider == "google",
            User.provider_id == provider_id
        ).first()

        if not user:
            user = User(provider="google", provider_id=provider_id, email=email)
            db.add(user)
            db.commit()
            db.refresh(user)

        # ✅ Return app session token
        access_token = create_access_token({"sub": str(user.id)})
        return {"access_token": access_token, "token_type": "bearer"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Google auth failed: {str(e)}")
