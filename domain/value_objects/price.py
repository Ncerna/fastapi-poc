class Price:
    def __init__(self, value: float):
        if value <= 0:
            raise ValueError("Price must be greater than 0")
        self.value = value