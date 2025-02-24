from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from backend.core.database import SessionLocal, User
from passlib.context import CryptContext
from fastapi import Form


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
    existing_user = db.query(User).filter((User.username == user.username) | (User.email == user.email)).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username or Email already exists")

    hashed_password = pwd_context.hash(user.password)
    new_user = User(username=user.username, email=user.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User registered successfully"}



@router.post("/login/")
def login_user(user: LoginUser, db: Session = Depends(get_db)):
    print(f"Received username: {user.username}, password: {user.password}")
    db_user = db.query(User).filter(User.username == user.username).first()
    print("Stored Password:", db_user.password)
    print("User Input Password:", user.password)
    hashed_test = pwd_context.hash("test_password")
    print(pwd_context.verify("test_password", hashed_test))  # Should return True

    if not db_user or not pwd_context.verify(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    return {"message": "Login successful", "user": {"username": user.username}}
