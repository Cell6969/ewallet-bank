import asyncio
from app.util import hash
from app.database.sql import async_session, engine
from app.model import DataPlan
from faker import Faker
from app.util.time import *

async def seed_data():
    async with async_session() as session:
        count = 0
        async with session.begin():
            print("Seed Data Plan....")
            data = [
                {
                    "name": '10 GB', 
                    "price": 100000,
                    "operator_card_id": 1,
                    "updated_at": get_datetime_naive()
                },
                {
                    "name": '25 GB', 
                    "price": 200000,
                    "operator_card_id": 1,
                    "updated_at": get_datetime_naive()
                },
                {
                    "name": '30 GB', 
                    "price": 300000,
                    "operator_card_id": 1,
                    "updated_at": get_datetime_naive()
                },
                {
                    "name": '40 GB', 
                    "price": 400000,
                    "operator_card_id": 1,
                    "updated_at": get_datetime_naive()
                },
                
                {
                    "name": '10 GB', 
                    "price": 100000,
                    "operator_card_id": 2,
                    "updated_at": get_datetime_naive()
                },
                {
                    "name": '25 GB', 
                    "price": 200000,
                    "operator_card_id": 2,
                    "updated_at": get_datetime_naive()
                },
                {
                    "name": '30 GB', 
                    "price": 300000,
                    "operator_card_id": 2,
                    "updated_at": get_datetime_naive()
                },
                {
                    "name": '40 GB', 
                    "price": 400000,
                    "operator_card_id": 2,
                    "updated_at": get_datetime_naive()
                },

                {
                    "name": '10 GB', 
                    "price": 100000,
                    "operator_card_id": 3,
                    "updated_at": get_datetime_naive()
                },
                {
                    "name": '25 GB', 
                    "price": 200000,
                    "operator_card_id": 3,
                    "updated_at": get_datetime_naive()
                },
                {
                    "name": '30 GB', 
                    "price": 300000,
                    "operator_card_id": 3,
                    "updated_at": get_datetime_naive()
                },
                {
                    "name": '40 GB', 
                    "price": 400000,
                    "operator_card_id": 3,
                    "updated_at": get_datetime_naive()
                },
            ]
            
            for d in data:
                data_plan = DataPlan(**d)
                session.add(data_plan)
                count+=1
        print(f"Success seed data plan! {count}")

if __name__ == "__main__":
    asyncio.run(seed_data())