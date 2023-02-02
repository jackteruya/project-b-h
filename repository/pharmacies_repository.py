from sqlalchemy.exc import NoResultFound

from infra.db import DBConnectionHandler
from infra.db.models import Pharmacies as PharmaciesModel
from src.pharmacies.data.interface import PharmaciesRepositoryInterface


class PharmaciesRepository(PharmaciesRepositoryInterface):
    def __init__(self):
        self._db_connection = DBConnectionHandler

    def get_all(self):
        try:
            with self._db_connection() as db_connection:
                data = db_connection.session.query(PharmaciesModel).all()
                return data

        except NoResultFound:
            return []
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()