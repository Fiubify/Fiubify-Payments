from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.controllers.wallets_controller import create_wallet, get_wallet_balance
from app.models.wallet import WalletSchema
from app.responses import ResponseModel, ErrorResponseModel

router = APIRouter()

@router.post("/", response_description="Created wallet address")
async def create_wallet_data():
  new_wallet = await create_wallet()

  return ResponseModel(new_wallet, "Wallet created successfully")
  
@router.get("/{address}", response_description="Wallet balance retrieved")
async def get_wallet_balance_data(address):
  balance = await get_wallet_balance(address)
  if balance:
    return ResponseModel(balance, "Wallet balance retrieved successfully")
<<<<<<< Updated upstream
  return ErrorResponseModel("Error occurred", 404, "No wallet found to match address")
=======
  return ErrorResponseModel("Error occurred", 404, "No wallet found to match address")

@router.post("/transaction", response_description="Transaction created")
async def post_transaction(transaction: TransactionModel):
  transaction_response = await create_transaction(transaction)

  if transaction_response and not "error" in transaction_response:
    return ResponseModel(transaction_response, "Transaction successful")
  return ErrorResponseModel("Error occurred", 400, "Transaction failed")
>>>>>>> Stashed changes
