from domain.entities.product import Product
from application.dtos.product.create_product_dto import CreateProductDto
from application.dtos.product.update_product_dto import UpdateProductDto
from application.dtos.product.product_response_dto import ProductResponseDto


class ProductMapper:

    @staticmethod
    def to_entity(dto: CreateProductDto) -> Product:
        return Product(
            id=None,
            name=dto.name,
            price=dto.price,
            stock=dto.stock
        )

    @staticmethod
    def update_entity(entity: Product, dto: UpdateProductDto) -> Product:

        if dto.name is not None:
            entity.name = dto.name

        if dto.price is not None:
            entity.price = dto.price

        if dto.stock is not None:
            entity.stock = dto.stock

        return entity

    @staticmethod
    def to_response(entity: Product) -> ProductResponseDto:
        return ProductResponseDto(
            id=entity.id,
            name=entity.name,
            price=entity.price,
            stock=entity.stock
        )

    @staticmethod
    def to_response_list(entities: list[Product]) -> list[ProductResponseDto]:
        return [ProductMapper.to_response(e) for e in entities]