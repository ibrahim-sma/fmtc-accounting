from datetime import datetime, timezone, timedelta
from jose import jwt
from app.core.config import settings, secret_key, algorithm, access_token_expire_minutes

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(
    minutes=access_token_expire_minutes
)
    to_encode.update({"exp": expire})
    return jwt.encode(
        to_encode,
        secret_key,
        algorithm=algorithm
    )
