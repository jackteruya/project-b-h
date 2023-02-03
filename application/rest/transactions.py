from typing import List

from fastapi import APIRouter

from src.transactions.domain.entity import Transactions
from src.transactions.domain.transactions_use_case import TransactionsUseCase

router: APIRouter = APIRouter(prefix="/transactions")


@router.get("", response_model=List[Transactions])
def get_all_transactions():
    """Endpoint to return all pharmacies"""

    return TransactionsUseCase().get_all()
