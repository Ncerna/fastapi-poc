
from pydantic import BaseModel

class ProductResponseDto(BaseModel):
    id: int
    name: str
    price: float
    stock: int