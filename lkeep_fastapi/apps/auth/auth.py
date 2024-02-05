import redis.asyncio
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import (
    CookieTransport,
    RedisStrategy,
    AuthenticationBackend,
)

from lkeep_fastapi.apps.auth.manager import get_user_manager
from lkeep_fastapi.core.models import User
from lkeep_fastapi.core.settings import settings

cookie_transport = CookieTransport(cookie_max_age=3600)

redis = redis.asyncio.from_url(
    f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}", decode_responses=True
)


def get_redis_strategy() -> RedisStrategy:
    return RedisStrategy(redis, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="cookie_redis",
    transport=cookie_transport,
    get_strategy=get_redis_strategy,
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)
