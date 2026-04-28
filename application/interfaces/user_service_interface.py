from abc import ABC, abstractmethod
from typing import List
from domain.entities.user import User


class IUserService(ABC):

    @abstractmethod
    def list_users(self) -> List[User]:
        pass