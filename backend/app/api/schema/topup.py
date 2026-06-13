from pydantic import BaseModel, EmailStr, field_validator, Field
from app.config import app_settings
from datetime import datetime

class TopupRequest(BaseModel):
    amount: int
    pin: str
    payment_method_code:str

    @field_validator('payment_method_code')
    @classmethod
    def valid_payment_method_code(cls, value:str) -> str:
        list_payment_method = ['bni_va', 'bca_va', 'bri_va']
        if value not in list_payment_method:
            raise ValueError("payment method code doesn't exists")
        
        return value