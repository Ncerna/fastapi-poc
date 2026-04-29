from typing import Generic, TypeVar, Optional

T = TypeVar("T")

class ApiResponse(Generic[T]):
    def __init__(self, data: Optional[T] = None, message: str = "OK", status: bool = True):
        self.data = data
        self.message = message
        self.status = status

    def to_dict(self):
        return {
            "status": self.status,
            "message": self.message,
            "data": self.data
        }