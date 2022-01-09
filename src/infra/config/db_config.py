from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler:
    """Sqlalchemy database connection"""

    def __init__(self) -> None:
        self.__connection_string = "sqlite:///storage.db"
        self.session = None

    def get_engine(self):
        """Return connection Engine
        >>> from src.infra.config import*
        >>> from src.infra.entities import *
        >>> db_conn = DBConnectionHandler()
        >>> engine = db_conn.get_engine()
        >>> engine
        Engine(sqlite:///storage.db)
        >>> Base.metadata.create_all(engine)
        :parram - None
        :return - engine connection to Database
        """
        engine = create_engine(self.__connection_string)
        return engine

    def __enter__(self):
        engine = create_engine(self.__connection_string)
        session_maker = sessionmaker()
        self.session = session_maker(bind=engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()  # pylint: disable=no-member
