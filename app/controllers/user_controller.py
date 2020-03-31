from uuid import uuid4

from app.models.user import User
from database.repository import save


class UserController:

    @classmethod
    def create(cls, **kwargs) -> User:
        return save(User(
            id=str(uuid4()),
            username=kwargs['username'],
            password=kwargs['password'],
            email=kwargs['email'],
            fullname=kwargs['fullname'],
            gender=kwargs['gender'],
            contact_number=kwargs['contact_number'],
            address=kwargs['address'],
        ))

    def find_user(self, username: str) -> list:
        return self._find_user_by_username(username)

    def _find_user_by_username(self, username: str) -> list:
        return User.query.filter_by(username=username).all()
