from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.infraestructure.database import Database
from app.api.routes import user_router, task_router, auth_router

from app.constants import ENV


@asynccontextmanager
async def lifespan(app: FastAPI):
    database = Database()
    if ENV == "development":
        await database.init_models()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(user_router)
app.include_router(task_router)
app.include_router(auth_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
