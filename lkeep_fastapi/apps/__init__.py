from fastapi import APIRouter

from .auth import router as auth_router


router = APIRouter(prefix="/apps")

router.include_router(router=auth_router, tags=["Auth"])
