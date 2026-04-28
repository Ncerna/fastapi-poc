from typing import List
from domain.entities.user import User
from application.interfaces.user_repository import IUserRepository


class UserRepository(IUserRepository):

    def __init__(self):
        self.users = [
            User(1, "Daniel", "daniel@test.com"),
            User(2, "Ana", "ana@test.com"),
        ]

    def get_all(self) -> List[User]:
        return self.users

    def get_by_id(self, user_id: int) -> User:
        for u in self.users:
            if u.id == user_id:
                return u
        return None

    