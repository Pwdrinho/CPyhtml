class Product:
    def __init__(self, code, description, partner, price, status):
        self.code = code
        self.description = description
        self.partner = partner
        self.price = price
        self.status = status

    def show(self):
        print(f"Code: {self.code}, Description: {self.description}, Partner: {self.partner}, Price: {self.price}, Status: {self.status}")
