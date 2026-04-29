class Stock:
    def __init__(self, value: int):
        if value < 0:
            raise ValueError("Stock cannot be negative")
        self.value = value

    def add(self, quantity: int):
        return Stock(self.value + quantity)

    def remove(self, quantity: int):
        if self.value - quantity < 0:
            raise ValueError("Insufficient stock")
        return Stock(self.value - quantity)