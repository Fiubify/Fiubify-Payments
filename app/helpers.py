def wallets_query_helper(wallet) -> dict:
  return {
    "id": str(wallet["_id"]),
    "address": wallet["address"],
    "private_key": wallet["private_key"],
    "user_id": wallet["user_id"]
  }