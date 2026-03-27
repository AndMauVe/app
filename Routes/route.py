from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from Core.database import get_db
from Models.user import User
from Schemas.user import UserCreate, UserOut

router = APIRouter()


@router.get("/ping", status_code=status.HTTP_200_OK)
async def get_pong():
    return {"message": "pong"}   


@router.get("/users", response_model=list[UserOut], status_code=status.HTTP_200_OK)
def list_users(db: Session = Depends(get_db)):
    return db.query(User).order_by(User.id.asc()).all()


@router.post("/users", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def create_user(payload: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == payload.email).first()
    if existing:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="El email ya existe")

    user = User(name=payload.name, email=payload.email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
