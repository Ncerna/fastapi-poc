from fastapi import APIRouter
from application.dtos.product.create_product_dto import CreateProductDto
from application.dtos.product.update_product_dto import UpdateProductDto
from application.contract.product_service_interface import IProductService

class ProductController:

    def __init__(self, service:IProductService):
        self.service = service
        self.router = APIRouter(prefix="/api/v1/products")
        self._register_routes()

    def _register_routes(self):

        @self.router.get("/")
        def get_all(page: int = 1, size: int = 10):
            return self.service.get_all(page, size)

        @self.router.get("/{product_id}")
        def get_by_id(product_id: int):
            return self.service.get_by_id(product_id)

        @self.router.post("/")
        def create(product: CreateProductDto):
            return self.service.create(product)

        @self.router.put("/{product_id}")
        def update(product_id: int, product: UpdateProductDto):
            return self.service.update(product_id, product)

        @self.router.delete("/{product_id}")
        def delete(product_id: int):
            return self.service.delete(product_id)