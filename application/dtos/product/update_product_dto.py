
from pydantic import BaseModel, Field
from typing import Optional

class UpdateProductDto(BaseModel):
    name: Optional[str] = Field(None, min_length=3)
    price: Optional[float] = Field(None, gt=0)
    stock: Optional[int] = Field(None, ge=0)