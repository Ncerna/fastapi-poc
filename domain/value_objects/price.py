class Price:
    def __init__(self, value: float):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.value = value