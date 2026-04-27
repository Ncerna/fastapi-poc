from fastapi import APIRouter

class ProductController:

    def __init__(self, service):
        self.service = service
        self.router = APIRouter(prefix="/api/v1/products")
        self._register_routes()

    def _register_routes(self):

        @self.router.get("/")
        def get_all():
            return self.service.get_all()

        @self.router.get("/{product_id}")
        def get_by_id(product_id: int):
            return self.service.get_by_id(product_id)

        @self.router.post("/")
        def create(product: dict):
            return self.service.create(product)

        @self.router.put("/{product_id}")
        def update(product_id: int, product: dict):
            return self.service.update(product)

        @self.router.delete("/{product_id}")
        def delete(product_id: int):
            return self.service.delete(product_id)