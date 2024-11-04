from sqlalchemy.orm import Session
from app.domain.repositories.user_repository import IUserRepository


class UserRepository(IUserRepository):
    def __init__(self, db: Session):
        self.db = db
