from sqlalchemy import Column, Integer, String,Float
from database import Base

class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    username= Column(String,unique=True)
    email=Column(String,index=True)
    hashed_password=Column(String)