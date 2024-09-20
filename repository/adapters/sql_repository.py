from __future__ import annotations
from typing import List

from repository.adapters.repository import AbstractUserRepository
from repository.model.user import User


class SQLAlchemyUserRepository(AbstractUserRepository):
    model = User

    def __init__(self, session=None):
        super().__init__()
        self._session = session

    def bind_session(self, session):
        self._session = session

    def add(self, user: User) -> None:
        self._session.add(user)

    def get_by_id(self, id: int) -> User:
        return self._session.query(self.model).filter_by(id=id).first()

    def get_by_username(self, user_name: str) -> List[User]:
        return self._session.query(self.model).filter_by(fullname=user_name).all()

    def get_by_account(self, employee_id: int) -> User:
        return self._session.query(self.model).filter_by(account=employee_id).first()

    def update(self, user_id: int, *args, **kwargs):
        self._session.query(User).filter_by(id=user_id).update(kwargs)
        return self.get_by_id(user_id)

    def commit(self):
        self._session.commit()
