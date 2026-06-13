from app.service.base import BaseService
from app.model import (
    Wallet, 
    PaymentMethod, 
    TransactionType, 
    Transaction
)
from sqlalchemy.ext.asyncio import AsyncSession 
from app.api.schema.topup import TopupRequest
from sqlalchemy import select
from app.core.exception import EntityNotFound, BadRequest, InvalidPin
from app.util.file import File
from app.util.hash import hash
from app.util.time import get_datetime_naive
import random
from app.core.log import logger
from sqlalchemy.orm import selectinload

class WalletService(BaseService[Wallet]):
    def __init__(self, session:AsyncSession):
        super().__init__(Wallet, session)

    async def add_balance_topup(self, user_id:int, data:TopupRequest):
        wallet = await self._pin_check(user_id, data.pin)
        transaction_type = (await self.session.execute(
            select(TransactionType).where(TransactionType.code == 'topup')
        )).scalar_one_or_none()
        payment_method = (await self.session.execute(
            select(PaymentMethod).where(PaymentMethod.code == data.payment_method_code)
        )).scalar_one_or_none()

        transaction = Transaction()
        transaction.user_id = user_id
        transaction.payment_method_id = payment_method.id
        transaction.transaction_type_id = transaction_type.id
        transaction.amount = data.amount

        return True
  
    """
    id: user id
    pin: pin for wallet of user
    """
    async def _pin_check(self, id:int, pin:str) -> Wallet:
        wallet = (await self.session.execute(
            select(Wallet)
                .where(Wallet.user_id == id)
                .options(selectinload(Wallet.user))
        )).scalar_one_or_none()

        if not wallet:
            raise EntityNotFound()
        
        if wallet.pin != pin:
            raise InvalidPin()
        
        return wallet

    
    async def _generate_card_number(self, length:int) -> str :
        result = "".join(str(random.randint(0, 9)) for _ in range(length))
        wallet = (await self.session.execute(
            select(Wallet).where(Wallet.card_number == result)
        )).scalar_one_or_none()

        if wallet:
            return await self._generate_card_number(length=length)
        
        return result
    