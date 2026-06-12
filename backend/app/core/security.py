from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.util.paseto import Credential
import time

security = HTTPBearer()

async def get_auth_user(credentials:HTTPAuthorizationCredentials = Depends(security)) -> dict:
    token = credentials.credentials
    try:
        payload = Credential.decode_token(token=token)
        if "exp" in payload:
            if (int(time.time()) > payload['exp']):
                raise HTTPException(
                        status_code=status.HTTP_401_UNAUTHORIZED,
                        detail="Token is Expired"
                    )
            return payload
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid Token"
            ) 
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token"
        )