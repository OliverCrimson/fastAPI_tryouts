from pydantic import BaseModel


class User(BaseModel):
    name: str
    id: int
    age: int


class Feedback(BaseModel):
    name: str
    message: str


class UserCreate(BaseModel):
    name: str
    email: str
    age: int = 1
    is_subscribed : bool = False
