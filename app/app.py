import os
from fastapi import FastAPI, Body, HTTPException, status

from routes.wallet import router as WalletRouter

app = FastAPI()
app.include_router(WalletRouter, tags=["Wallet"], prefix="/wallet")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}