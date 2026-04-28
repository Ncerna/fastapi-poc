from fastapi import APIRouter


class UserController:

    def __init__(self, service):
        self.service = service
        self.router = APIRouter(prefix="/api/v1/users")
        self._register_routes()

    def _register_routes(self):

        @self.router.get("/")
        def get_all():
            return self.service.list_users()

       