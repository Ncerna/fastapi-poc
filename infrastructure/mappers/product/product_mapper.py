from domain.entities.product.product import Product
from infrastructure_app.models.product_model import ProductModel


class ProductMapper:
    @staticmethod
    def to_entity(model: ProductModel) -> Product:
        return Product(
            id=model.id,
            name=model.name,
            price=float(model.price),
            stock=model.stock,
           
        )

    @staticmethod
    def to_model(entity: Product) -> ProductModel:
        model = ProductModel(
            name=entity.name,
            price=entity.price,
            stock=entity.stock,
           
        )

        if entity.id is not None:
            model.id = entity.id

        return model