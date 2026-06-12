from app.service.base import BaseService
from app.model import User, Wallet
from sqlalchemy.ext.asyncio import AsyncSession 
from app.api.schema.auth import RegisterRequest
from sqlalchemy import select
from app.core.exception import AlreadyCreated
from app.util.file import File
from app.util.hash import hash
from app.util.time import get_datetime_naive
import random
from app.core.log import logger

class WalletService(BaseService[Wallet]):
    def __init__(self, session:AsyncSession):
        super().__init__(Wallet, session)
    
    async def _generate_card_number(self, length:int) -> str :
        result = "".join(str(random.randint(0, 9)) for _ in range(length))
        # wallet = (await self.session.execute(
        #     select(Wallet).where(Wallet.card_number == result)
        # )).scalar_one_or_none()

        logger.info(result)

        # if wallet:
        #     return await self._generate_card_number(length=length)
        
        return result