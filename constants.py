import os

ENV = os.environ.get("ENV", "development")
DATABASE_URL = os.environ.get("DATABASE_URL")