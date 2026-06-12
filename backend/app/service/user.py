from app.service.base import BaseService
from app.model import User, Wallet
from sqlalchemy.ext.asyncio import AsyncSession 
from app.api.schema.auth import RegisterRequest, LoginRequest
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from app.core.exception import AlreadyCreated, EntityNotFound, ClientNotAuthorized
from app.util.file import File
from app.util.hash import hash, verify_hash
from app.util.time import get_datetime_naive
from app.service.wallet import WalletService
from app.util.paseto import Credential
from datetime import timedelta
from app.api.schema.auth import UserResponse

class UserService(BaseService[User]):
    def __init__(self, session:AsyncSession, wallet_service: WalletService):
        super().__init__(User, session)
        self.wallet_service = wallet_service

    async def register(self, data: RegisterRequest):
        existing_user = (await self.session.execute(
            select(User)
                .where(User.email == data.email)
        )).scalar_one_or_none()

        if existing_user:
            raise AlreadyCreated()
        
        file_ktp = None
        file_profile_picture = None

        if data.ktp:
            file_ktp = File.save_image_from_b64(data.ktp, 'user','ktp')
        
        if data.profile_picture:
            file_profile_picture = File.save_image_from_b64(data.profile_picture, 'user', 'prf')

        user = User(
            name = data.name,
            email = data.email,
            username = data.email,
            password = hash(data.password),
            profile_picture = file_profile_picture,
            ktp = file_ktp,
            verified = True if file_ktp else False,
            is_admin = False,
            updated_at = get_datetime_naive()
        )

        self.session.add(user)
        await self.session.flush()

        wallet = Wallet(
            user_id = user.id,
            balance = 0,
            pin = data.pin,
            card_number = await self.wallet_service._generate_card_number(16)
        )

        self.session.add(wallet)
        await self.session.commit()
        await self.session.refresh(user, attribute_names=['wallet'])

        token = Credential.generate_token({
            'email':user.email,
            'name': user.name,
            'id': user.id
        }, expired=timedelta(hours=1))

        return UserResponse(
            id=user.id,
            name=user.name,
            email=user.email,
            ktp=user.ktp,
            profile_picture=user.profile_picture,
            token=token,
            created_at=user.created_at,
            updated_at=user.updated_at,
            balance=user.wallet.balance,
            card_number=user.wallet.card_number,
            pin=user.wallet.pin,
            token_expired_in=int(timedelta(hours=1).total_seconds())
        )
    
    async def login(self, data:LoginRequest):
        user = (await self.session.execute(
            select(User)
                .where(User.email == data.email)
                .options(selectinload(User.wallet))
        )).scalar_one_or_none()

        if not user:
            raise EntityNotFound()
        
        if not verify_hash(user.password, data.password):
            raise ClientNotAuthorized()
        
        token = Credential.generate_token({
            'email':user.email,
            'name': user.name,
            'id': user.id
        }, expired=timedelta(hours=1))

        return UserResponse(
            id=user.id,
            name=user.name,
            email=user.email,
            ktp=user.ktp,
            profile_picture=user.profile_picture,
            token=token,
            created_at=user.created_at,
            updated_at=user.updated_at,
            balance=user.wallet.balance,
            card_number=user.wallet.card_number,
            pin=user.wallet.pin,
            token_expired_in=int(timedelta(hours=1).total_seconds())
        )