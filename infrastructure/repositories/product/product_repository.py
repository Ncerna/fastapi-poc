from application.interfaces.product_repository_interface import IProductRepository
from infrastructure_app.models.product_model import ProductModel
from infrastructure.mappers.product.product_mapper import ProductMapper
from domain.entities.product.product import Product
from typing import List, Optional

class ProductRepository(IProductRepository):

    def get_all(self) -> List[Product]:
        queryset = ProductModel.objects.all()
        return [ProductMapper.to_entity(obj) for obj in queryset]

    def get_by_id(self, product_id: int) -> Optional[Product]:
        obj = ProductModel.objects.get(id=product_id)
        return ProductMapper.to_entity(obj)

    def create(self, product: Product) -> Product:
        model = ProductMapper.to_model(product)
        model.save()
        return ProductMapper.to_entity(model)

    def update(self, product: Product) -> Product:
        model = ProductModel.objects.get(id=product.id)

        updated = ProductMapper.to_model(product)

        model.name = updated.name
        model.price = updated.price
        model.stock = updated.stock

        model.save()
        return ProductMapper.to_entity(model)

    def delete(self, product_id: int) -> bool:
        obj = ProductModel.objects.get(id=product_id)
        obj.delete()
        return True