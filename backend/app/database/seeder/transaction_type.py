import asyncio
from app.util import hash
from app.database.sql import async_session, engine
from app.model import TransactionType, TransactionAction
from faker import Faker
from app.util.time import *

async def seed_data():
    async with async_session() as session:
        count = 0
        async with session.begin():
            print("Seed Transaction Type....")
            data = [
                {
                    "name": 'Transfer', 
                    "code": 'transfer',
                    "action": TransactionAction.DR,
                    "updated_at": get_datetime_naive()
                },
                {
                    "name": 'Internet', 
                    "code": 'internet',
                    "action": TransactionAction.DR,
                    "updated_at": get_datetime_naive()
                },
                {
                    "name": 'Topup', 
                    "code": 'top_up',
                    "action": TransactionAction.CR,
                    "updated_at": get_datetime_naive()
                },
                {
                    "name": 'Receive', 
                    "code": 'receive',
                    "action": TransactionAction.CR,
                    "updated_at": get_datetime_naive()
                },
            ]
            
            for d in data:
                transaction_type = TransactionType(**d)
                session.add(transaction_type)
                count+=1
        print(f"Success seed Transaction Type! {count}")

if __name__ == "__main__":
    asyncio.run(seed_data())