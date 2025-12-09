import os
import secrets
from fastapi import status, HTTPException
from datetime import datetime, timedelta, timezone
from typing import Optional

from jose import jwt, JWTError
from passlib.context import CryptContext

class JWTSecurity:
    def __init__(self):
        self.__secret = os.getenv("JWT_SECRET_KEY")
        self.__algorithm = os.getenv("JWT_ALGORITHM")
        self.__jwt_access_token_expiration_minutes = 15

        self.__crypt_context = CryptContext(schemes=['argon2'])
    
    def hash_password(self, password: str):
        return self.__crypt_context.hash(password)
    
    def verify_password(self, password: str, hashed_password: str):
        return self.__crypt_context.verify(password, hashed_password)
    
    def create_access_token(self, subject: dict, expires_delta: Optional[timedelta] = None):
        date_now = datetime.now(timezone.utc)

        expire = date_now + (expires_delta or timedelta(minutes=self.__jwt_access_token_expiration_minutes))

        payload = {
            "sub": str(subject["id"]),
            "username": subject["username"],
            "email": subject["email"],
            "iat": int(date_now.timestamp()),
            "exp": int(expire.timestamp())
        }

        return jwt.encode(payload, self.__secret, self.__algorithm)
    
    def decode_access_token(self, token: str) -> dict:
        try:
            payload = jwt.decode(token, self.__secret, algorithms=[self.__algorithm])
            return payload
        except JWTError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido ou expirado")
        
    def generate_refresh_token(self) -> str:
        return secrets.token_hex(32)