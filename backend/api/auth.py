from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from backend.core.database import SessionLocal, User
from passlib.context import CryptContext
from fastapi import Form
from backend import logger
import traceback

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class RegisterUser(BaseModel):
    username: str
    email: EmailStr
    password: str

class LoginUser(BaseModel):
    username: str
    password: str

@router.post("/register/")
def register_user(user: RegisterUser, db: Session = Depends(get_db)):
    # Check if user already exists
    try: 
        existing_user = db.query(User).filter((User.username == user.username) | (User.email == user.email)).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Username or Email already exists")

        hashed_password = pwd_context.hash(user.password)
        new_user = User(username=user.username, email=user.email, password=hashed_password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return {"message": "User registered successfully"}
    
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")


@router.post("/login/")
def login_user(user: LoginUser, db: Session = Depends(get_db)):
    try:
        logger.info(f"Received username: {user.username}, password: {user.password}")
        db_user = db.query(User).filter(User.username == user.username).first()

        if not db_user:
            raise HTTPException(status_code=400, detail="Invalid username or password")
        
        if not pwd_context.verify(user.password, db_user.password):
            raise HTTPException(status_code=400, detail="Invalid username or password")


        logger.info(f"Stored Password: {db_user.password}")
        logger.info(f"User Input Password: {user.password}")
        hashed_test = pwd_context.hash("test_password")
        logger.info(pwd_context.verify("test_password", hashed_test))  # Should return True

        
        return {"message": "Login successful", "user": {"username": user.username}}
    
    except SQLAlchemyError as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")