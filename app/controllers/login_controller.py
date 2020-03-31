from uuid import uuid4

from app.controllers.user_controller import UserController
from app.models.login_model import Login
from app.models.user import User
from database.repository import save


class LoginController:

    @classmethod
    def create(cls, username: str, password: str) -> Login:
        return save(Login(id=str(uuid4()), username=username, password=password))

    def validate_login(self, username: str, password: str) -> Login:
        saved_user = self._validate_username(username)
        if not password == saved_user.get_password():
            raise Exception('Senha incorreta')
        return self.create(username, password)

    def _validate_username(self, username: str) -> User:
        user_controller = UserController()
        saved_user = user_controller.find_user(username)
        if not len(saved_user):
            raise Exception('Usuário não encontrado')
        return saved_user[0]
