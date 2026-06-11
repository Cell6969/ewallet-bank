import asyncio
from app.util import hash
from app.database.sql import async_session, engine
from app.model import OperatorCard, OperatorCardStatus
from faker import Faker
from app.util.time import *

async def seed_data():
    async with async_session() as session:
        count = 0
        async with session.begin():
            print("Seed Operator....")
            data = [
                {
                    "name": 'Telkomsel', 
                    "status": OperatorCardStatus.ACTIVE,
                    "thumbnail": 'operator/telkomsel.png',
                    "updated_at": get_datetime_naive()
                },
                {
                    "name": 'Indosat', 
                    "status": OperatorCardStatus.ACTIVE,
                    "thumbnail": 'operator/indosat.png',
                    "updated_at": get_datetime_naive()
                },
                {
                    "name": 'Singtel', 
                    "status": OperatorCardStatus.ACTIVE,
                    "thumbnail": 'operator/singtel.png',
                    "updated_at": get_datetime_naive()
                },
            ]
            
            for d in data:
                operator = OperatorCard(**d)
                session.add(operator)
                count+=1
        print(f"Success seed data operator! {count}")

if __name__ == "__main__":
    asyncio.run(seed_data())