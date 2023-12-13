import jwt
from base.base_schema import BaseSchema


class UserSchema(BaseSchema):
    id: int
    login: str
    password: str
    phone: str
    email: str
    is_staff: bool
    is_superuser:bool

    def generate_token(self) -> dict:
        return {
            "access_token": jwt.encode(
                {"login": self.login, "password": self.password},
                "my-32-character-ultra-secure-and-ultra-long-secret",
            )
        }

    def validate_password(self, password: str) -> bool:
        return self.password == password
