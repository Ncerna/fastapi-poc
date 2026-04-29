class Stock:
    def __init__(self, value: int):
        if value < 0:
            raise ValueError("Stock cannot be negative")
        self.value = value