from uuid import uuid4

from app.models.login_model import Login
from database.repository import save


class LoginController:

    @classmethod
    def create(cls, username: str, password: str) -> Login:
        return save(Login(id=str(uuid4()), username=username, password=password))
