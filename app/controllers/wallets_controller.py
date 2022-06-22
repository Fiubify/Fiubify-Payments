from bson.objectid import ObjectId

import requests
from eth_account import Account
import secrets

from app.database import wallets_collection

async def create_wallet() -> str:
  private_key = '0x' + secrets.token_hex(32)
  address = Account.from_key(private_key).address

  wallet_data = {
    "address": address,
    "private_key": private_key
  }

  await wallets_collection.insert_one(wallet_data)
  return {"address": address}

async def get_wallet_balance(address: str) -> dict:
  wallet = await wallets_collection.find_one({"address": address})

  if wallet:
    req = {
      "jsonrpc":"2.0",
      "method": "eth_getBalance",
      "params": [
        address,
        "latest"
      ],
      "id":1
    }

    res = requests.post("https://kovan.infura.io/v3/7754e74d5b25437285d1e9fc42b41932", json=req)
    balance = int(res.json()['result'], 0)*10**(-18)

    return {"balance": balance}