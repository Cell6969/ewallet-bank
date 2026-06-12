from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference
from app.config import app_settings
from typing import cast
from contextlib import asynccontextmanager
from app.database.sql import engine
from sqlalchemy import text
from app.core.log import logger
from app.api.router import master_router
from app.core.exception import add_exception_handler
from fastapi.staticfiles import StaticFiles

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Try Connect to DB")

    try:
        async with engine.connect() as conn:
            await conn.execute(text('SELECT 1'))
        print('Successfully Connect to Database')

        logger.info('App is Running')
    except Exception as e:
        print('Failed Connect to DB')
        print(f"Error: {e}")

    yield

app = FastAPI(
    title=app_settings.APP_NAME,
    lifespan=lifespan,
    docs_url=None,
    redoc_url=None,
    version="1.0.0",
)
# Public file
app.mount('/storage', StaticFiles(directory='public'), name='public')

# Router
app.include_router(master_router)

# Exception
add_exception_handler(app=app)

@app.get('/docs', include_in_schema=False)
def docs():
    return get_scalar_api_reference(
        openapi_url=cast("str", app.openapi_url),
        title="Services Docs"
    )