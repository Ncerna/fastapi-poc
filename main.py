from fastapi import FastAPI
import os
import django

#os.environ.setdefault(
   # "DJANGO_SETTINGS_MODULE",
   # "infrastructure_ul.django.config.settings"
#)

django.setup()

# 📦 Imports correctos
from infrastructure.repositories.django_product_repository import DjangoProductRepository
from application.services.product_service import ProductService
from presentation.controllers.product_controller import ProductController

# 🚀 FastAPI app
app = FastAPI()

# 🔥 Composition Root
repository = DjangoProductRepository()
service = ProductService(repository)
controller = ProductController(service)

# 🌐 Routes
app.include_router(controller.router)