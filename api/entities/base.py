import pytz
from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

from constants import TIMEZONE

Base = declarative_base()


class CommonFields(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True, autoincrement="auto")
    created_at = Column(DateTime(timezone=True), default=datetime.now(tz=pytz.timezone(TIMEZONE)))
    updated_at = Column(DateTime(timezone=True), default=datetime.now(tz=pytz.timezone(TIMEZONE)))
