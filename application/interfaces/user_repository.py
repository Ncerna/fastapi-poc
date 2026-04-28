from abc import ABC, abstractmethod
from typing import List
from domain.entities.user import User


class IUserRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[User]:
        pass