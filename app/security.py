from pwdlib import PasswordHash
import os
from dotenv import load_dotenv
import jwt
from datetime import datetime, timedelta, timezone


password_hash = PasswordHash.recommended()

def hash_password(password: str) -> str:
    return password_hash.hash(password)

def verify_password(plain_password, hashed_password) -> bool:
    return password_hash.verify(plain_password, hashed_password)

load_dotenv()

SECRETE_KEY = os.getenv("SECRETE_KEY")

if not SECRETE_KEY:
    raise ValueError(""SECRETE KEY is missing, please set it in your .env file"")

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(user_id:int) -> str:
     expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
     payload = {
        "sub":str(user_id),
        "exp": expire
     }
     return jwt.encode(payload, SECRETE_KEY, algorith=ALGORITHM)

def decode_access_token(token:str)-> int|None:
    try:
        payload = jwt.decode(token, SECRETE_KEY, algoriths=[ALGORITHM])
        return int(payload["sub"])
    except jwt.InvalidTokenError:
        return None

    


   

     