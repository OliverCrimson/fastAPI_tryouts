import uuid

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from starlette.status import HTTP_404_NOT_FOUND
# from app.secure import pwd_context
from app.models.core import User, Token
from app.models.schemas import UserAuth


from app.secure import pwd_context


def make_token(db: Session, user_data: UserAuth):
    user: User = db.scalar(select(User).where(User.email == user_data.email))
    if not user:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    if not pwd_context.verify(user_data.password, user.hashed_password):
        raise HTTPException(status_code=400,
                            detail="Incorrect username or password")
    token: Token = Token(user_id=user.id, access_token=str(uuid.uuid4()))
    db.add(token)
    db.commit()
    return {"access_token": token.access_token}
