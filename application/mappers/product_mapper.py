from domain.entities.product import Product
from domain.value_objects.price import Price
from domain.value_objects.stock import Stock
from infrastructure.django_infra.models.product_model import ProductModel

from application.dtos.product.create_product_dto import CreateProductDto
from application.dtos.product.update_product_dto import UpdateProductDto
from application.dtos.product.product_response_dto import ProductResponseDto


class ProductMapper:

    # DTO → ENTITY (CREATE)
    @staticmethod
    def from_create_dto(dto: CreateProductDto) -> Product:
        return Product(
            id=None,
            name=dto.name,
            price=Price(dto.price),
            stock=Stock(dto.stock)
        )

    # DTO → ENTITY (UPDATE parcial)
    @staticmethod
    def update_entity(entity: Product, dto: UpdateProductDto) -> Product:

        if dto.name is not None:
            entity.name = dto.name

        if dto.price is not None:
            entity.price = Price(dto.price)

        if dto.stock is not None:
            entity.stock = Stock(dto.stock)

        return entity

    # ENTITY → RESPONSE DTO
    @staticmethod
    def to_response(entity: Product) -> ProductResponseDto:
        return ProductResponseDto(
            id=entity.id,
            name=entity.name,
            price=entity.price.value,
            stock=entity.stock.value
        )

    # ENTITY → DJANGO MODEL
    @staticmethod
    def to_model(entity: Product) -> ProductModel:
        return ProductModel(
            id=entity.id,
            name=entity.name,
            price=entity.price.value,
            stock=entity.stock.value
        )

    # MODEL → ENTITY
    @staticmethod
    def to_entity(model: ProductModel) -> Product:
        return Product(
            id=model.id,
            name=model.name,
            price=Price(model.price),
            stock=Stock(model.stock)
        )
    