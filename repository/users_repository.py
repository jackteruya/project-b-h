from sqlalchemy.exc import NoResultFound

from infra.db import DBConnectionHandler
from infra.db.models import Users as UsersModel
from src.users.data.interface import UserRepositoryInterface


class UsersRepository(UserRepositoryInterface):
    """Patients Repository"""

    def __init__(self):
        self._db_connection = DBConnectionHandler

    def get_by_username(self, username: str):
        try:
            with self._db_connection() as db_connection:
                data = (
                    db_connection.session.query(UsersModel)
                    .filter_by(username=username)
                    .first()
                )
                return data

        except NoResultFound:
            return []
        except:
            db_connection.session.rollback()
        finally:
            db_connection.session.close()

    def create_user(self, username: str, password: str):
        try:
            with self._db_connection() as db_connection:
                new_user = UsersModel(username=username, password=password)
                db_connection.session.add(new_user)
                db_connection.session.commit()
                db_connection.session.refresh(new_user)
                return new_user

        except NoResultFound:
            return []
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()
