from pydantic import BaseModel, EmailStr, field_validator, Field
from app.config import app_settings
from datetime import datetime

class RegisterRequest(BaseModel):
    name: str
    email: EmailStr
    password: str = Field(
        min_length=6,
        max_length=20,
        # pattern=r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]+$",
        # description='Minimum password is 6 character, contains 1 Uppercase, 1 lowercase, 1 number and 1 symbol'
    )
    pin: str = Field(
        min_length=6,
        max_length=6,
        pattern=r"^\d+$"
    )
    ktp: str | None
    profile_picture: str | None

class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(
        min_length=6,
        max_length=20,
        # pattern=r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]+$",
        # description='Minimum password is 6 character, contains 1 Uppercase, 1 lowercase, 1 number and 1 symbol'
    )


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    ktp: str
    profile_picture: str | None
    created_at: datetime
    updated_at: datetime
    balance: int
    card_number: str
    pin: str
    token: str
    token_expired_in: int
    token_type:str = 'Bearer'


    @field_validator('ktp')
    @classmethod
    def convert_ktp_to_url(cls, value:str) -> str:
        if value:
            return f"{app_settings.APP_DOMAIN}/storage/{value}"
        return value
    
    @field_validator('profile_picture')
    @classmethod
    def convert_profile_picture_to_url(cls, value:str) -> str:
        if value:
            return f"{app_settings.APP_DOMAIN}/storage/{value}"
        return value

