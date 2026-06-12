from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware

def set_middleware(app:FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    except_route = [
        '/auth/login',
        '/auth/register',
        '/docs',
        '/redoc',
        '/openapi.json'
    ]

    class TokenMiddleware(BaseHTTPMiddleware):
        async def dispatch(self, request:Request, call_next):
            if request.method == "OPTIONS":
                return await call_next(request)
            path = request.url.path.rstrip('/')
            if path not in except_route:
                x_token = request.headers.get("Authorization")
                if not x_token:
                    return JSONResponse(
                        status_code=401, 
                        content={"detail": "token not found"}
                    )
                
            return await call_next(request)

    app.add_middleware(TokenMiddleware)