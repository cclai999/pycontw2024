
if __name__ == "__main__":
    from repository.adapters.repository import MemoryUserRepository
    from repository.model.user import User
    from repository.model.user import set_user_repo
    user_repo = MemoryUserRepository()

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

