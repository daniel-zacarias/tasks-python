from contextlib import asynccontextmanager
from fastapi import FastAPI
from api.connectors.db_connection_session import Database
from api.controllers import user_router, task_router, auth_router

from constants import ENV


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
