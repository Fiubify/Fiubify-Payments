from bson.objectid import ObjectId
from pydantic import BaseModel, Field

class WalletSchema(BaseModel):
  address: str = Field(...)
  private_key: str = Field(...)

  class Config:
    schema_extra = {
      "example": {
        "address": "0xC216dC1b18BA24Cb157CF116e1e0cD2b785f5454",
        "private_key": "0x8da4ef21b864d2cc526dbdb2a120bd2874c36c9d0a1fb7f8c63d7f7a8b41de8f"
      }
    }
