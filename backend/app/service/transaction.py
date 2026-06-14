from sqlalchemy.ext.asyncio import AsyncSession
from app.service.wallet import WalletService
from app.api.schema.transaction import TopupRequest
from app.model import Wallet, Transaction,TransactionType, PaymentMethod
from sqlalchemy.orm import selectinload
from sqlalchemy import select
import secrets
import string
from app.util.time import get_datetime_naive
from app.core.exception import *
import midtransclient
from app.config import midtrans_settings
from app.helper.midtrans import MidtransUtility

class TransactionService:
    def __init__(self,session:AsyncSession,wallet_service: WalletService):
        self.session = session
        self.wallet_service = wallet_service
        self.midtrans_settings = midtrans_settings


    async def topup(self,user_id:int, data:TopupRequest):
        wallet = await self.wallet_service._pin_check(user_id, data.pin)
        transaction_type = (await self.session.execute(
            select(TransactionType).where(TransactionType.code == 'top_up')
        )).scalar_one_or_none()
        if not transaction_type:
            return EntityNotFound()
        
        payment_method = (await self.session.execute(
            select(PaymentMethod).where(PaymentMethod.code == data.payment_method_code)
        )).scalar_one_or_none()
        if not payment_method:
            return EntityNotFound()

        try:
            transaction = Transaction()
            transaction.user_id = user_id
            transaction.payment_method_id = payment_method.id
            transaction.transaction_type_id = transaction_type.id
            transaction.amount = data.amount
            transaction.transaction_code = self._generate_transaction_code()
            transaction.description = f"Top up via {payment_method.name}"
            transaction.status = "pending"
            transaction.updated_at = get_datetime_naive()
            self.session.add(transaction)

            # call midtrans 
            params = MidtransUtility.build_params(
                user=wallet.user, transaction=transaction, payment_method=payment_method
            )
            result = self._call_midtrans(params=params)
            await self.session.commit()
            await self.session.refresh(transaction)
            return result
        except Exception as e:
            self.session.rollback()
            raise HTTPException(
                status_code=500,
                detail="Failed to topup wallet"
            )
    
    def _call_midtrans(self,params:dict) -> dict: 
        snap = midtransclient.Snap(
            is_production=self.midtrans_settings.MIDTRANS_IS_PRODUCTION,
            server_key=self.midtrans_settings.MIDTRANS_SERVER_KEY
        )
        transaction = snap.create_transaction(parameters=params)
        return transaction
    
    def _generate_transaction_code(self,length:int = 10):
        characters = string.ascii_letters + string.digits
        random_str = ''.join(secrets.choice(characters) for _ in range(length))
        return random_str.capitalize()
