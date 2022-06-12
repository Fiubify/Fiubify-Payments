import motor.motor_asuncio

mongodb_address = os.environ.get("MONGODB_URI", "mongodb://mongodb:27017")

if "MONGODB_URI" in os.environ:
  mongodb_address = os.environ.get("MONGODB_URI")
  db_name = "payments-staging"
else:
  mongodb_address = "mongodb://mongodb:27017"
  db_name = "payments-test"

client = motor.motor_asyncio.AsyncIOMotorClient(mongodb_address)
db = client[db_name]

wallets_collection = db.get_collection("wallets")