from sqlalchemy.exc import NoResultFound

from infra.db import DBConnectionHandler
from infra.db.models import Users as UsersModel
from src.users.data.interface import UserRepositoryInterface


class UsersRepository(UserRepositoryInterface):
    """Patients Repository"""

    def __init__(self):
        self._db_connection = DBConnectionHandler

    def get_by_uuid(self, uuid: str):
        try:
            with self._db_connection() as db_connection:
                data = db_connection.session.query(UsersModel).get(uuid)
                return data

        except NoResultFound:
            return []
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()
