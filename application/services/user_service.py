
from application.interfaces.user_repository import IUserRepository
from application.contract.user_service_interface import IUserService
from application.dtos.user.user_response_dto import UserResponseDto
from application.shared.wappers.paginated_response import PaginatedResponse
from application.mappers.user_mapper import UserMapper

class UserService(IUserService):

    def __init__(self, repository: IUserRepository):
        self.repository_ = repository

    def list_users(self, page: int = 1, size: int = 10, search: str = None):
     users, total = self.repository_.get_all(page, size, search) 

     return PaginatedResponse[UserResponseDto](
            items=[UserMapper.to_response(u) for u in users], 
            total=total,
            page=page,
            size=size
        )
        