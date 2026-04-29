
from application.contract.product_service_interface import IProductService
from application.interfaces.product_repository import IProductRepository
from application.mappers.product_mapper import ProductMapper
from application.shared.wappers.paginated_response import PaginatedResponse
from application.shared.wappers.response import ApiResponse
from application.dtos.product.create_product_dto import CreateProductDto
from application.dtos.product.update_product_dto import UpdateProductDto
from application.dtos.product.product_response_dto import ProductResponseDto
from application.errors.app_exception import AppException


class ProductService(IProductService):

    def __init__(self, repository: IProductRepository):
        self.repository = repository

    def get_all(self, page: int = 1, size: int = 10):
        products, total = self.repository.get_all(page, size)

        return PaginatedResponse[ProductResponseDto](
            items=[ProductMapper.to_response(p) for p in products],
            total=total,
            page=page,
            size=size
        )
    def get_by_id(self, product_id: int):
     product = self.repository.get_by_id(product_id)
     if not product:
            raise AppException("Product not found", 404)

     return ApiResponse(  data=ProductMapper.to_response(product),
            message="OK"
         )
      

    def create(self, dto: CreateProductDto):
        entity = ProductMapper.from_create_dto(dto)
        return ApiResponse( self.repository.create(entity),"Created successfully")


    def update(self, product_id: int, dto: UpdateProductDto):
        entity = self.repository.get_by_id(product_id)

        if not entity:
            raise AppException( "Product not found")

        entity = ProductMapper.update_entity(entity, dto)
        return ApiResponse(self.repository.update(entity))
    

    def delete(self, product_id: int):
        if not self.repository.get_by_id(product_id):
            raise AppException("Product not found", 404)
        self.repository.delete(product_id)

        return ApiResponse( data=True,  message="Deleted successfully")