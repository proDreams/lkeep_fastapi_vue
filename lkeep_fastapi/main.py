import uvicorn
from fastapi import FastAPI

from .apps import router as apps_router


app = FastAPI()

app.include_router(router=apps_router)


def start():
    uvicorn.run(app="lkeep_fastapi.main:app", reload=True)
