from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.authschemas import UserCreate, UserResponse
from Cruds.authcrud import create_user, get_user_by_username, get_user_by_email
from database import get_db
from utils.hashing import verify_password
from utils.jwt_token import create_access_token
from fastapi.security import OAuth2PasswordRequestForm

auth_router = APIRouter()

@auth_router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_username(db, username=user.username)
    db_email = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    if db_email:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db, user)
    

@auth_router.post("/login")
def login_user(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = get_user_by_username(db, form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
