from typing import List
from domain.entities.user import User
from application.interfaces.user_repository import IUserRepository
from application.contract.user_service_interface import IUserService


class UserService(IUserService):

    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    def list_users(self) -> List[User]:
        return self.user_repository.get_all()