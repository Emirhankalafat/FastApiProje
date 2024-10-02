from fastapi import FastAPI
from pydantic import BaseModel
import models.authmodels as authmodels
from database import engine
from routes.auth import auth_router
from fastapi.middleware.cors import CORSMiddleware





    
app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth_router, prefix="/auth", tags=["auth"])

@app.get("/")
def read_root():
    return {"Hello":"World"}

