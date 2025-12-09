from fastapi import Request, status
from fastapi.responses import JSONResponse
from fastapi.routing import APIRoute
from starlette.middleware.base import BaseHTTPMiddleware
from src.anticorrupcao.auth.jwt_security import JWTSecurity


class ProtectedRoute(APIRoute):

    def get_route_handler(self) -> callable:
        get_route_handler = super().get_route_handler()
        
        async def custom_route_handler(request: Request):
            endpoint = self.endpoint

            is_protected = getattr(endpoint, "_protected", False)

            if not is_protected:
                return await get_route_handler(request)
            
            auth_header = request.headers.get("Authorization")

            if not auth_header or not auth_header.startswith("Bearer "):
                return JSONResponse({"detail": "Token não informado"}, status_code=status.HTTP_401_UNAUTHORIZED)
            
            token = auth_header.split(" ", 1)[1].strip()

            try:
                payload = JWTSecurity().decode_access_token(token)
            except Exception as e:
                msg = getattr(e, "detail", str(e))
                return JSONResponse({"detail": msg}, status_code=status.HTTP_401_UNAUTHORIZED)
            
            request.state.user = payload

            return await get_route_handler(request)
        
        return custom_route_handler