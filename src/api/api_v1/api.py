from fastapi import APIRouter

from .endpoints import users

router = APIRouter()
router.include_router(router=users.router,prefix="/users")