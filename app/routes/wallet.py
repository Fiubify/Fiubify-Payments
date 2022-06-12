from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.controllers.wallets_controller import create_wallet

router = APIRouter()