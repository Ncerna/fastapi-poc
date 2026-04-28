from fastapi import FastAPI
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')


django.setup()
from presentation.module import get_user_controller, get_product_controller

django.setup()
#  FastAPI app
app = FastAPI()
#  Composition Root
app.include_router(get_user_controller().router)
app.include_router(get_product_controller().router)