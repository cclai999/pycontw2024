# Database ORM.
import logging

from sqlalchemy import (
    Table, Column, Integer, String, Text, Boolean, DateTime,
    func
)
from sqlalchemy.orm import registry

from repository.utility.time_tools import get_local_time
from repository.model.user import User as DomainUser


logger = logging.getLogger(__name__)

DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'

mapper_registry = registry()

orm_users = Table(
    'user', mapper_registry.metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('account', Integer, unique=True, nullable=False, comment="員工號", index=True),
    Column('password', String(150), nullable=True, comment="密碼"),
    Column('fun_group', Integer, nullable=True, comment="功能群"),
    Column('fullname', String(100), nullable=False, comment="姓名", index=True),
    Column('roles', Text, nullable=False, default='user', comment="角色權限"),
    Column('is_active', Boolean, nullable=False, default=True, comment="帳號啟用狀態"),
    Column('last_login', DateTime, nullable=True, default=get_local_time, comment="前次登入時間"),
    Column('created_at', DateTime, nullable=False, default=get_local_time, comment="記錄建立時間", server_default=func.now())
)


def start_mappers():
    logger.info("Starting mappers")
    mapper_registry.map_imperatively(DomainUser, orm_users)

