from sqlalchemy import Column, DateTime, Integer, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class CommonFields(Base):
    __abstract__ = True 

    id = Column(Integer, primary_key=True, index=True, autoincrement="auto")
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())