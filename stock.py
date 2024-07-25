

from typing import Dict
from product import Product


class Stock:
    """
    A class to represent the stock.

    Methods
    -------
    def add_product(self, product: Product):
        Adds a product to the store.
    def find_product(self, product_name: str) -> Product:
        Search for the product in stock.
    def setup_store(self):
        Stock the list of products in a dictionary.

    """

    def __init__(self):
        """
        Initialize stock
        """

        self.products: Dict[str, Product] = {}

    def add_product(self, product: Product):
        """
                Adds a product to the store.

                Parameters
                ----------
                product : Product
                    The product to be added to the store."""

        self.products[product.name] = product

    def find_product(self, product_name: str) -> Product:

        """
        Search for the product in stock.
        :param product_name: str, name of product
        :return: Product
        """
        return self.products.get(product_name)

    def setup_store(self):
        """
        Stock the list of products in a dictionary.
        :return:
        """
        products = {
            "Clémentine": ("Fruit", 6, 2.9),
            "Datte": ("Fruit", 4, 7.0),
            "Grenade": ("Fruit", 3, 3.5),
            "Kaki": ("Fruit", 3, 4.5),
            "Kiwi": ("Fruit", 5, 3.5),
            "Mandarine": ("Fruit", 6, 2.8),
            "Orange": ("Fruit", 8, 1.5),
            "Pamplemousse": ("Fruit", 8, 2.0),
            "Poire": ("Fruit", 5, 2.5),
            "Pomme": ("Fruit", 8, 1.5),
            "Carotte": ("Vegetable", 7, 1.3),
            "Choux de Bruxelles": ("Vegetable", 4, 4.0),
            "Chou vert": ("Vegetable", 12, 2.5),
            "Courge butternut": ("Vegetable", 6, 2.5),
            "Endive": ("Vegetable", 5, 2.5),
            "Épinard": ("Vegetable", 4, 2.6),
            "Poireau": ("Vegetable", 5, 1.2),
            "Potiron": ("Vegetable", 6, 2.5),
            "Radis noir": ("Vegetable", 10, 5.0),
            "Salsifis": ("Vegetable", 3, 2.5)
        }

        for name, (category, stock, price) in products.items():
            self.add_product(Product(name, category, stock, price))

    def __str__(self) -> str:
        """
        Print product in stock.
        :return:Update of stock
        """


        stock_lines = ["Stock:"]
        for product in self.products.values():
             stock_lines.append(str(product))
        return "\n".join(stock_lines)




