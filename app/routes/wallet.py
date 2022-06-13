from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from controllers.wallets_controller import create_wallet
from models.wallet import WalletSchema
from responses import ResponseModel, ErrorResponseModel

router = APIRouter()

@router.post("/", response_description="Created wallet address")
async def create_wallet_data():
  new_wallet = await create_wallet()

  return ResponseModel(new_wallet, "Wallet created successfully")
  