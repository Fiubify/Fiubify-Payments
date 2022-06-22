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
async def get_wallet_balance_data(address)
  balance = await get_wallet_balance(address)
  if balance:
    return ResponseModel(balance, "Wallet balance retrieved successfully")
  return ErrorResponseModel("Error occurred", 404, "No wallet found to match address")