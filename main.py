from fastapi import FastAPI

from infrastructure.repositories.in_memory_product_repository import InMemoryProductRepository
from application.services.product_service import ProductService
from presentation.controllers.product_controller import ProductController

app = FastAPI()

# 🔥 Composition Root (Dependency Injection manual)
repository = InMemoryProductRepository()
service = ProductService(repository)
controller = ProductController(service)


app.include_router(controller.router)