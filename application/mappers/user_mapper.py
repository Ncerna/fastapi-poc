from domain.entities.user import User
from application.dtos.user.user_response_dto import UserResponseDto 


class UserMapper:
    # ENTITY → RESPONSE DTO
    @staticmethod
    def to_response(entity: User) -> UserResponseDto:
        return UserResponseDto(
            
            name=entity.name,
            email=entity.email
        )
