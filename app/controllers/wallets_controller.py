from bson.objectid import ObjectId

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
