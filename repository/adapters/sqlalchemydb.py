from math import ceil
from typing import Union, Tuple
import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, Session

from repository.adapters.orm import start_mappers

engine = None
db_session: Union[Session, scoped_session] = scoped_session(sessionmaker())
Base = None


def init_engine(uri, options):
    global engine
    engine = create_engine(uri, **options)
    db_session.configure(bind=engine)
    return engine


def init_db():
    """Create all tables needed for the first time
    若是第一次使用, 可以呼叫此 function 建立相關 table
    :return: None
    """

    global Base
    from repository.adapters.orm import mapper_registry
    start_mappers()
    Base = mapper_registry.generate_base()
    Base.query = db_session.query_property()
    Base.metadata.create_all(bind=engine)


def write_into_database(use_flush=False):
    try:
        if use_flush:
            db_session.flush()
        else:
            db_session.commit()
    except Exception as e:
        logging.critical(f"DB Error: {e}")
        db_session.rollback()
        raise Exception(f"Database Error: {e}")


def pagination(query, page, per_page) -> Tuple[list, int, int]:
    """提供分頁查詢的功能
    :param query:
    :param page:
    :param per_page:
    :return:
    result: list of query record
    total_pages: int
    record_count: int
    """
    total = query.count()
    return (
        query.limit(per_page).offset((page - 1) * per_page).all(),
        int(ceil(total / float(per_page))) if per_page > 0 else None,
        total
    )
