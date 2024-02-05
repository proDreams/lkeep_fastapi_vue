from fastapi import APIRouter

from .auth import fastapi_users, auth_backend
from .schemas import UserRead, UserCreate

router = APIRouter(prefix="/auth")

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    tags=["auth"],
)

router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    tags=["register"],
)
