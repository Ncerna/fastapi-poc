
from pydantic import BaseModel
from typing import List
from application.dtos.product.product_response_dto import ProductResponseDto

class ProductListDto(BaseModel):
    items: List[ProductResponseDto]
    total: int
    page: int
    size: int