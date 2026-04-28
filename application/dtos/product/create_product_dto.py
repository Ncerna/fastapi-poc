
from pydantic import BaseModel, Field

class CreateProductDto(BaseModel):
    name: str = Field(..., min_length=3)
    price: float = Field(..., gt=0)
    stock: int = Field(..., ge=0)