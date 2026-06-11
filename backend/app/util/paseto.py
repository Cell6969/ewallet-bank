from datetime import datetime, timedelta,timezone
import pyseto
from pyseto import Key
from app.config import app_settings
import json

class Credential:
    key = Key.new(version=4, purpose='local', key=app_settings.APP_KEY)
    
    @staticmethod
    def generate_token(data:dict, expired:timedelta = timedelta(minutes=10)) -> str:
        exp_timestamp = int((datetime.now(timezone.utc) + expired).timestamp())
        payload = {
            **data,
            "exp": exp_timestamp
        }
        token = pyseto.encode(
            key=Credential.key,
            payload=payload,
        )

        return token.decode('utf-8')

    @staticmethod
    def decode_token(token:str) -> dict:
        data = pyseto.decode(
            token=token,
            keys=Credential.key
        )
        return json.loads(data.payload)