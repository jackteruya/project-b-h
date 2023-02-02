import os

from fastapi import APIRouter

from application.rest import patients, pharmacies, transactions, users
from dotenv import load_dotenv


load_dotenv()

router = APIRouter(prefix=f"/api/{os.getenv('VERSION')}")


router.include_router(patients.router, tags=["Patients"])
router.include_router(pharmacies.router, tags=["Pharmacies"])
router.include_router(transactions.router, tags=["Transactions"])
router.include_router(users.router, tags=["Users"])
