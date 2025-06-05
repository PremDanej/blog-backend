from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash:

    def get_password_hash(self: str):
        return pwd_context.hash(self)

    def verify_password(self: str, hashed_password: str):
        return pwd_context.verify(self, hashed_password)
