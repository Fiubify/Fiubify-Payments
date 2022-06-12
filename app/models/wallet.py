from bson.objectid import ObjectId
from pydantic import BaseModel, Field

# Wraps around an ObjectId to allow Pydantic structure validation
class PydanticObjectId(ObjectId):
  @classmethod
  def __get_validators__(cls):
    yield cls.validate

  @classmethod
  def validate(cls, v):
    if not isinstance(v, ObjectId):
      raise TypeError("ObjectId required")
    return str(v)

class WalletSchema(BaseModel):
  address: str = Field(...)
  private_key: str = Field(...)
  user_id: PydanticObjectId = Field(...)

  class Config:
    schema_extra = {
      "example": {
        "address": "0xC216dC1b18BA24Cb157CF116e1e0cD2b785f5454",
        "private_key": "0x8da4ef21b864d2cc526dbdb2a120bd2874c36c9d0a1fb7f8c63d7f7a8b41de8f",
        "user_id": "7Wx30Z2qRFTSnWWvG5dkmd8WhD42"
      }
    }

# Specifies the expected contents of a create_wallet request's body
class CreateWalletModel(BaseModel):
  user_id: str = Field(...)

  class Config:
    schema_extra = {
      "example": {
        "user_id": "7Wx30Z2qRFTSnWWvG5dkmd8WhD42"
      }
    }