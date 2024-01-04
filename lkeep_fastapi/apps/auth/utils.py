from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_users.db import SQLAlchemyUserDatabase

from lkeep_fastapi.core.database import Database
from lkeep_fastapi.core.models import User


async def get_user_db(
    session: AsyncSession = Depends(Database.scoped_session_dependency),
):
    yield SQLAlchemyUserDatabase(session, User)
