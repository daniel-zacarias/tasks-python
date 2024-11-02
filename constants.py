import os

ENV = os.environ.get("ENV", "development")
DATABASE_URL = os.environ.get("DATABASE_URL")
SECRET_KEY = os.environ.get("SECRET_KEY")
ACCESS_TOKEN_EXPIRE_MINUTES  = os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES", 30)
TIMEZONE = "America/Sao_Paulo"