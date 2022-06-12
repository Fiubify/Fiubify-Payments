from bson.objectid import ObjectId
from database import wallets_collection

from eth_account import Account
import secrets

async def create_wallet(user_id: str) -> str:
  private_key = '0x' + secrets.token_hex(64)
  account = Account.from_key(private_key)

  wallet_data = {
    address: account.address,
    private_key: private_key,
    user_id: user_id
  }

  wallet = await wallets_collection.insert_one(wallet_data)
  return wallet.address