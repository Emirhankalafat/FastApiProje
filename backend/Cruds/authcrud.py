from sqlalchemy.orm import Session
from models.authmodels import User
from schemas.authschemas import UserCreate
from utils.hashing import get_password_hash

def create_user(db:Session,user:UserCreate):
    hashed_password=get_password_hash(user.password)
    db_user=User(username=user.username,email=user.email,hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_username(db:Session,username:str):
    return db.query(User).filter(User.username==username).first()
def get_user_by_email(db:Session,email:str):
    return db.query(User).filter(User.email==email).first()