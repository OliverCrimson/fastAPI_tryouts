from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.controllers.tokens import make_token
from app.models import schemas
from app.models.database import get_db


router = APIRouter()


@router.post("", response_model=schemas.Token, status_code=201)
def create_token(user_data: schemas.UserAuth, db: Session = Depends(get_db)):
    return make_token(db=db, user_data=user_data)
