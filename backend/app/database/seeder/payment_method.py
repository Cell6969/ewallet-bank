import asyncio
from app.util import hash
from app.database.sql import async_session, engine
from app.model import User,PaymentMethod
from faker import Faker
from app.util.time import *

fake = Faker('id_ID')

async def seed_data():
    async with async_session() as session:
        count = 0
        async with session.begin():
            print("Seed Payment Method....")
            data = [
                {"name": 'Bank BCA', 'code': 'bca_va', 'status': 'active', 'updated_at': get_datetime_naive()},
                {"name": 'Bank BNI', 'code': 'bni_va', 'status': 'active','updated_at': get_datetime_naive()},
                {"name": 'Bank BRI', 'code': 'bri_va', 'status': 'active','updated_at': get_datetime_naive()},
            ]
            
            for d in data:
                payment_method = PaymentMethod(**d)
                session.add(payment_method)
                count+=1
        print(f"Success seed data! {count}")

if __name__ == "__main__":
    asyncio.run(seed_data())