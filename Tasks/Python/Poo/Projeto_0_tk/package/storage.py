from package.product import Product
import json



class LeituraCodigoBarras:
    def __init__(self):
        self.products = []
        try:
            with open("database/products.json", "r") as arquivo_json:
                product_data = json.load(arquivo_json)
                self.products = [Product(**data) for data in product_data]
        except FileNotFoundError:
            pass

    def insertProduct(self, code, description, partner, price, status):
        new_product = Product(code, description, partner, price, status)
        self.products.append(new_product)

    def record(self):
        with open("database/products.json", "w") as arquivo_json:
            product_data = [vars(product) for product in self.products]
            json.dump(product_data, arquivo_json)

    def clear_terminal(self):
        subprocess.run(["clear"])

