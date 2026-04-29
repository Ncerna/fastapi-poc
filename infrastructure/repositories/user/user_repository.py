from typing import List
from domain.entities.user import User
from application.interfaces.user_repository import IUserRepository


class UserRepository(IUserRepository):
    def __init__(self):
        self.users = [
            User(1, "Daniel", "daniel@test.com"),
            User(2, "Ana", "ana@test.com"),
        ]

    def get_all(self, page: int = 1, size: int = 10, search: str = None) -> List[User]:
        total = len(self.users)
        start = (page - 1) * size
        end = start + size
        users_page = self.users[start:end]
        return users_page, total 

    