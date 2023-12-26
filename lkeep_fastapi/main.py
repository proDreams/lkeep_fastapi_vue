import uvicorn
from fastapi import FastAPI

app = FastAPI()


def start():
    uvicorn.run(app="lkeep_fastapi.main:app", reload=True)
