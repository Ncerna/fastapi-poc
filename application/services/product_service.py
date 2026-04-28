from application.interfaces.product_service_interface import IProductService
from application.interfaces.product_repository_interface import IProductRepository
from domain.entities.product import Product

class ProductService(IProductService):

    def __init__(self, repository: IProductRepository):
        self.repository = repository

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, product_id: int):
        return self.repository.get_by_id(product_id)

    def create(self, product: Product):
        return self.repository.create(product)

    def update(self, product: Product):
        return self.repository.update(product)

    def delete(self, product_id: int):
        return self.repository.delete(product_id)