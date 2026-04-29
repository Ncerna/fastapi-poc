from abc import ABC, abstractmethod
from application.shared.wappers.paginated_response import PaginatedResponse


class IUserService(ABC):

    @abstractmethod
    def list_users(self,page: int = 1, size: int = 10, search:str =None) -> PaginatedResponse:
        pass