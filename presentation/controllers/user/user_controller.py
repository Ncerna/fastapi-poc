from fastapi import APIRouter
from application.contract.user_service_interface import IUserService

class UserController:

    def __init__(self, service:IUserService):
        self.service = service
        self.router = APIRouter(prefix="/api/v1/users")
        self._register_routes()

    def _register_routes(self):

        @self.router.get("/")
        def get_all(page: int = 1, size: int = 10, search:str =None):
            return self.service.list_users(page, size, search)

       