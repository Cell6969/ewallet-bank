from pydantic import BaseModel, EmailStr, field_validator
from app.config import app_settings

class RegisterRequest(BaseModel):
    name: str
    email: EmailStr
    password: str
    pin: str
    ktp: str | None
    profile_picture: str | None



class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    ktp: str
    profile_picture: str | None

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

