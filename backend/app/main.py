from .routes import auth as auth_routes
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from . import database
from .routes import weight as weight_routes
from .database import engine, Base
from .models import weight, user

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

# Mount the weights router
app.include_router(weight_routes.router)

app.include_router(auth_routes.router)

@app.get("/")
def root():
    return JSONResponse(content={"message": "The Journey Backend Running 🚀"}, media_type="application/json; charset=utf-8")
