from sqlalchemy.exc import NoResultFound

from infra.db import DBConnectionHandler
from infra.db.models import Transactions as TransactionsModel
from src.transactions.data.interface import TransactionsRepositoryInterface


class TransactionsRepository(TransactionsRepositoryInterface):
    def __init__(self):
        self._db_connection = DBConnectionHandler

    def get_all(self):
        try:
            with self._db_connection() as db_connection:
                data = db_connection.session.query(TransactionsModel).all()
                return data

        except NoResultFound:
            return []
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()
