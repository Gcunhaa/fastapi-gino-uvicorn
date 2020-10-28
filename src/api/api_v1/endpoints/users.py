from typing import Any, List

from fastapi import APIRouter

from schemas.user import User, UserCreate, UserUpdate
from models.user import User as ORMUser

router = APIRouter()

@router.get('/', response_model=List[User])
async def read_users(
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
        Retrieve users.
    """
    users = await ORMUser.query.limit(limit).offset(skip).gino.all()
    return users

@router.post('/', response_model=User)
async def create_user(
    request : UserCreate
) -> Any:
    """
    Create user
    """
    new_user : ORMUser = await ORMUser.create(**request.dict())
    return User.from_orm(new_user)

@router.get('/{id}', response_model=User)
async def read_user(
    id: int
) -> Any:
    """
    Retrieve user by id
    """
    user : ORMUser = await ORMUser.get_or_404(id)
    return User.from_orm(user)

@router.put('/{id}', response_model=User)
async def update_user(
    id: int,
    request: UserUpdate
) -> Any:
    """
    Update user
    """
    user : ORMUser= await ORMUser.get_or_404(id)
    updated_fields : User = User.from_orm(request)
    await user.update(**updated_fields.dict(skip_defaults=True)).apply()
    return User.from_orm(user)