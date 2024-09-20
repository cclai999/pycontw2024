from __future__ import annotations
import abc

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from repository.model.user import User


class AbstractUserRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, u: User):
        raise NotImplementedError

    @abc.abstractmethod
    def get_by_id(self, id) -> User:
        raise NotImplementedError

    @abc.abstractmethod
    def get_by_username(self, username) -> User:
        raise NotImplementedError

    @abc.abstractmethod
    def get_by_account(self, employee_id) -> User:
        raise NotImplementedError


_user_list = list()


class MemoryUserRepository(AbstractUserRepository):
    def __init__(self, user_list: list = None):
        if user_list is not None:
            self._users = user_list
        else:
            self._users = _user_list

    def add(self, user: User):
        self._users.append(user)

    def get_by_id(self, id) -> User:
        result = [u for u in self._users if u.id == id]
        return result[0] if (len(result)>=1) else None

    def get_by_username(self, username) -> [User]:
        return [u for u in self._users if u.username == username]

    def get_by_account(self, employee_id) -> User:
        result = [u for u in self._users if u.account == employee_id]
        return result[0] if (len(result) >= 1) else None

    def update(self, user_id: int, *args, **kwargs) -> User:
        user = self.get_by_id(user_id)
        for k, v in kwargs.items():
            setattr(user, k, v)
        return user

    def commit(self):
        pass
