from bson.objectid import ObjectId

import requests

from eth_account import Account
from web3 import Web3

import secrets

from app.database import wallets_collection
from app.models.wallet import TransactionModel, PaymentModel

INFURA_URL = "https://kovan.infura.io/v3/7754e74d5b25437285d1e9fc42b41932"
ORG_WALLET_ADDRESS = "0xC216dB1b18B44Cb157CF116e1e0cD2b785f54564"
MAX_FEE_PER_GAS = '250'
MAX_PRIORITY_FEE_PER_GAS = '3'

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

    res = requests.post(INFURA_URL, json=req)
    balance = int(res.json()['result'], 0)*10**(-18)

    return {"balance": balance}

async def execute_payment(payment: PaymentModel) -> dict:
  from_address = payment.from_address
  from_wallet = await wallets_collection.find_one({"address": from_address})

  if from_wallet:
    return _transfer(from_address, from_wallet['private_key'], ORG_WALLET_ADDRESS, payment.amount)

async def execute_transaction(transaction: TransactionModel) -> dict:
  from_address = transaction.from_address
  to_address = transaction.to_address
  amount = transaction.amount

  from_wallet = await wallets_collection.find_one({"address": from_address})
  to_wallet = await wallets_collection.find_one({"address": to_address})

  if from_wallet and to_wallet:
    return _transfer(from_address, from_wallet['private_key'], to_address, amount)

async def execute_withdrawal(withdrawal: TransactionModel) -> dict:
  from_address = withdrawal.from_address
  from_wallet = await wallets_collection.find_one({"address": from_address})

  if from_wallet:
    return _transfer(from_address, from_wallet['private_key'], withdrawal.to_address, withdrawal.amount)

def _transfer(from_wallet, private_key, to_wallet, amount):
  web3_provider = _web3_provider()

  nonce = web3_provider.eth.getTransactionCount(from_wallet)
  transaction = {
    'type': '0x2',
    'nonce': nonce,
    'from': from_wallet,
    'to': to_wallet,
    'value': web3_provider.toWei(amount, 'ether'),
    'maxFeePerGas': web3_provider.toWei(MAX_FEE_PER_GAS, 'gwei'),
    'maxPriorityFeePerGas': web3_provider.toWei(MAX_PRIORITY_FEE_PER_GAS, 'gwei'),
    'chainId': web3_provider.eth.chain_id
  }

  gas = web3_provider.eth.estimateGas(transaction)
  transaction['gas'] = gas

  signed_transaction = web3_provider.eth.account.sign_transaction(transaction, private_key)
  transaction_response = web3_provider.eth.send_raw_transaction(signed_transaction.rawTransaction)

  return transaction_response

def _web3_provider():
  return Web3(Web3.HTTPProvider(INFURA_URL))