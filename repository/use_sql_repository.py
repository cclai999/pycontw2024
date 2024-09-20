from pathlib import Path
from repository.adapters.sqlalchemydb import init_engine, init_db
from repository.adapters.sql_repository import SQLAlchemyUserRepository
from repository.adapters.orm import start_mappers
from repository.adapters.sqlalchemydb import db_session

if __name__ == "__main__":
    PROJECT_BASE_DIR = Path(__file__).parent.absolute()
    SQLITE_PATH = PROJECT_BASE_DIR / "local.db"
    DB_URI = f"sqlite:///{SQLITE_PATH}"
    ENGINE_OPTIONS={ "echo": True}

    init_engine(DB_URI, options=ENGINE_OPTIONS)
    ans = input("請輸入你想要的操作 1)建立資料庫 2)新增 User Data :"
                "   ")
    if ans == "1":
        init_db()
    elif ans == "2":
        start_mappers()
        from repository.model.user import User
        from repository.model.user import set_user_repo

        user_repo = SQLAlchemyUserRepository(db_session)

        set_user_repo(user_repo)

        user_list = [
            User(id=0, account=13284, fullname="Max", password="1234", fun_group=4900),
            User(id=1, account=13285, fullname="John", password="qwer", fun_group=4902),
            User(id=2, account=13286, fullname="Susan", password="asdf", fun_group=4907),
        ]

        for u in user_list:
            user_repo.add(u)
        user_repo.commit()
        print(f"user[0]:{user_repo.get_by_id(0).to_dict()}")
    else:
        print("輸入錯誤")
