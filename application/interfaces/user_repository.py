from abc import ABC, abstractmethod
from typing import List
from domain.entities.user import User


class IUserRepository(ABC):

    @abstractmethod
    def get_all(self,page: int = 1, size: int = 10, search:str =None) -> List[User]:
        pass