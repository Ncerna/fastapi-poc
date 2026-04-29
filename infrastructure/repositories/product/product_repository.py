from application.interfaces.product_repository import IProductRepository
from infrastructure.django_infra.models.product_model import ProductModel
from application.mappers.product_mapper import ProductMapper
from domain.entities.product import Product

from typing import List, Tuple, Optional


class ProductRepository(IProductRepository):

    def get_all(self, page: int = 1, size: int = 10) -> Tuple[List[Product], int]:
        queryset = ProductModel.objects.all()

        total = queryset.count()

        start = (page - 1) * size
        end = start + size

        items = queryset[start:end]

        return (
            [ProductMapper.to_entity(obj) for obj in items],
            total
        )

    def get_by_id(self, product_id: int) -> Optional[Product]:
        obj = ProductModel.objects.filter(id=product_id).first()

        if not obj:
            return None

        return ProductMapper.to_entity(obj)

    def create(self, product: Product) -> Product:
        model = ProductMapper.to_model(product)
        model.save()
        return ProductMapper.to_entity(model)

    def update(self, product: Product) -> Product:
        model = ProductModel.objects.filter(id=product.id).first()

        if not model:
            raise Exception("Product not found")

        model.name = product.name
        model.price = product.price
        model.stock = product.stock

        model.save()

        return ProductMapper.to_entity(model)

    def delete(self, product_id: int) -> bool:
        obj = ProductModel.objects.filter(id=product_id).first()

        if not obj:
            return False

        obj.delete()
        return True