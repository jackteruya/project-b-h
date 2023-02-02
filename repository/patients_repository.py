from sqlalchemy.exc import NoResultFound

from infra.db import DBConnectionHandler
from infra.db.models import Patients as PatientsModel
from src.patients.data.interface import PatientsRepositoryInterface


class PatientsRepository(PatientsRepositoryInterface):
    def __init__(self):
        self._db_connection = DBConnectionHandler

    def get_all(self):
        try:
            with self._db_connection() as db_connection:
                data = db_connection.session.query(PatientsModel).all()
                return data

        except NoResultFound:
            return []
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()
