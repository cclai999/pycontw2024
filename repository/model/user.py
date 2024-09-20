from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional

from repository.utility.time_tools import get_local_time

_user_repo = None

class Settings:
    DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
    DATE_FORMAT = "%Y-%m-%d"


def set_user_repo(repo):
    global _user_repo
    _user_repo = repo


@dataclass
class User(object):
    account: int  # employee_id
    fullname: str
    password: str = ''
    fun_group: int = field(default_factory=int)
    id: int = None
    roles: str = 'user'
    is_active: bool = True
    last_login: Optional[datetime] = None
    created_at: datetime = field(default_factory=get_local_time)

    @property
    def identity(self):
        """
        ``identity`` instance attribute or property
        that provides the unique id of the user instance
        """
        return self.id

    @property
    def rolenames(self):
        """
        ``rolenames`` instance attribute or property
        that provides a list of strings that describe the roles
        attached to the user instance
        """
        result = [role.strip() for role in self.roles.split(",")]
        if len(result) == 0:
            result = []
        return result

    def is_valid(self):
        return self.is_active

    def to_dict(self):
        return {
            "user_id": self.id,
            "employee_id": self.account,
            "username": self.fullname,
            "roles": self.rolenames,
            "function group": self.fun_group,
            "is_valid": self.is_active,
            "last_login": "no data" if self.last_login is None else self.last_login.strftime(Settings.DATETIME_FORMAT),
            "created_at": self.created_at.strftime(Settings.DATETIME_FORMAT)
        }

    @classmethod
    def update_last_login_time_by_id(cls, id, login_time):
        global _user_repo
        return _user_repo.update(id, last_login=login_time)
