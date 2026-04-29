from domain.value_objects.price import Price
from domain.value_objects.stock import Stock

class Product:
    def __init__(self, id: int, name: str, price: Price, stock: Stock):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock

    def update_price(self, new_price: Price):
        self.price = new_price

    def increase_stock(self, quantity: int):
        self.stock = self.stock.add(quantity)