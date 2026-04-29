from fastapi import FastAPI
from application.errors.app_exception import AppException
from infrastructure.exceptions.handler import app_exception_handler
from infrastructure.exceptions.validation import validation_exception_handler
from fastapi.exceptions import RequestValidationError
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')


django.setup()
from presentation.module import get_user_controller, get_product_controller

django.setup()
#  FastAPI app
app = FastAPI()
#  Composition Root
app.add_exception_handler(AppException, app_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.include_router(get_user_controller().router)
app.include_router(get_product_controller().router)
