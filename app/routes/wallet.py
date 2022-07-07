from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.controllers.wallets_controller import create_wallet, get_wallet_balance, execute_transaction, execute_withdrawal, execute_payment
from app.models.wallet import WalletSchema, TransactionModel, PaymentModel
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
  return ErrorResponseModel("Error occurred", 404, "No wallet found to match address")

@router.post("/payment", response_description="Payment created")
async def post_payment(payment: PaymentModel):
  payment_response = await execute_payment(payment)

  if payment_response and not "error" in payment_response:
    return ResponseModel(payment_response, "Payment successful")
  return ErrorResponseModel("Error occurred", 400, "Payment failed")

@router.post("/transaction", response_description="Transaction created")
async def post_transaction(transaction: TransactionModel):
  transaction_response = await execute_transaction(transaction)

  if transaction_response and not "error" in transaction_response:
    return ResponseModel(transaction_response, "Transaction successful")
  return ErrorResponseModel("Error occurred", 400, "Transaction failed")

@router.post("/withdrawal", response_description="Transaction created")
async def post_withdrawal(withdrawal: TransactionModel)
  withdrawal_response = await execute_withdrawal(withdrawal)

  if withdrawal_response and not "error" in withdrawal_response:
    return ResponseModel(withdrawal_response, "Withdrawal successful")
  return ErrorResponseModel("Error occurred", 400, "Withdrawal failed")