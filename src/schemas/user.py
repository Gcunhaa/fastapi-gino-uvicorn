from typing import Optional

from pydantic import BaseModel

class UserBase(BaseModel):
    nickname: str 

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass


#DATABASE BASE
class User(UserBase):
    id: Optional[int]

    class Config:
        orm_mode = True


