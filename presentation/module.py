# USERS
from infrastructure.repositories.user.user_repository import UserRepository
from application.services.user_service import UserService
from presentation.controllers.user.user_controller import UserController

# PRODUCTS
from infrastructure.repositories.product.product_repository import ProductRepository
from application.services.product_service import ProductService
from presentation.controllers.product.product_controller import ProductController


def get_user_controller():
  
    return UserController(UserService(UserRepository()))


def get_product_controller():
    return ProductController(ProductService(ProductRepository()))
   