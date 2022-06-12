from bson.objectid import ObjectId

from eth_account import Account
import secrets

from database import wallets_collection

async def create_wallet(user_id: str) -> str:
  private_key = '0x' + secrets.token_hex(64)
  account = Account.from_key(private_key)

  wallet_data = {
    address: account.address,
    private_key: private_key,
    user_id: user_id
  }

  wallet = await wallets_collection.insert_one(wallet_data)
  return {address: wallet.address, user_id: wallet.user_id}