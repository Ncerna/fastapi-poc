from typing import Generic, TypeVar, Optional
from pydantic import BaseModel
from fastapi import FastAPI

T = TypeVar("T")

class ApiResponse(BaseModel, Generic[T]):
    status: str = "success"
    code: str = "OK"
    message: str = "Operación exitosa"
    data: Optional[T] = None