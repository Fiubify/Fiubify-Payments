import os
from fastapi import FastAPI, Body, HTTPException, status

from app.routes.wallet import router as WalletRouter

app = FastAPI()
app.include_router(WalletRouter, tags=["Wallet"], prefix="/wallet")
