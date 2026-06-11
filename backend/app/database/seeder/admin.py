import asyncio
from app.util import hash
from app.database.sql import async_session, engine
from app.model import User
from faker import Faker


fake = Faker('id_ID')

async def seed_data():
    async with async_session() as session:
        async with session.begin():
            print("Seed Admin....")
            data = {
                "name" : "Sysadmin",
                "email": "sysadmin@help.com",
                "password": hash.hash('admin123'),
                "username": "sysadmin123",
                "verified": True,
                "ktp": '327502220999001',
                "profile_picture": fake.image_url(width=200, height=200),
                "is_admin": True
            }
            user = User(**data)

            session.add(user)
    
        print(f"Success seed data!")

if __name__ == "__main__":
    asyncio.run(seed_data())