from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from controllers.wallets_controller import create_wallet
from models.wallet import WalletSchema, CreateWalletModel
from responses import ResponseModel, ErrorResponseModel

router = APIRouter()

@router.post("/", response_description="Wallet created for target user")
async def create_wallet_data(wallet: CreateWalletModel = Body(...)):
  wallet_data = jsonable_encoder(wallet)
  new_wallet = await create_wallet(wallet_data)

  return ResponseModel(new_wallet, "Wallet created successfully")