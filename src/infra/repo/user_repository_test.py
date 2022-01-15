from src.infra.config import DBConnectionHandler
from .user_repository import UserRepository


user_repository = UserRepository()
db_connection_handler = DBConnectionHandler()


def test_insert_user():
    """Should Insert User"""

    name = "Paulo1eer232"
    password = "902ert3"
    engine = db_connection_handler.get_engine()

    new_user = user_repository.insert_user(name, password)
    query_user = engine.execute(
        "SELECT * FROM users WHERE id = '{}';".format(new_user.id)
    ).fetchone()
    print(new_user)
    print(query_user)

    engine.execute("DELETE FROM users WHERE id='{}'".format(new_user.id))

    assert new_user.id == query_user.id
    assert new_user.name == query_user.name
    assert new_user.password == query_user.password
