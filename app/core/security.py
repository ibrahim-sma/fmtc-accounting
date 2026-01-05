from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

MAX_PASSWORD_LENGTH = 72

def normalize_password(password: str) -> str:
    """
    bcrypt supports max 72 bytes.
    We safely trim AFTER encoding.
    """
    password_bytes = password.encode("utf-8")
    return password_bytes[:MAX_PASSWORD_LENGTH].decode("utf-8", errors="ignore")

def hash_password(password: str) -> str:
    normalized = normalize_password(password)
    return pwd_context.hash(normalized)

def verify_password(password: str, hashed: str) -> bool:
    normalized = normalize_password(password)
    return pwd_context.verify(normalized, hashed)
