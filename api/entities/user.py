from sqlalchemy import Column, String
from api.entities.base import CommonFields
from sqlalchemy.orm import relationship

class User(CommonFields):
    __tablename__ = "users"

    name = Column(String, index=True, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    tasks = relationship("Task", back_populates="user")
