from typing import Dict, List

from customer import Customer
from product import Product
from customer import Customer
from stock import  Stock

class Store:
    """
    A class to represent a store.

    Attributes
    ----------
    products : dict
        A dictionary to store products with product name as the key.
    customers : list
        A list to store the customers visiting the store.

    Methods
    -------
    add_product(product: Product) -> None:
        Adds a product to the store.
    find_product(product_name: str) -> Product:
        Finds and returns a product by its name.
    add_customer(customer: Customer) -> None:
        Adds a customer to the store.
    customer_visit() -> None:
        Handles the interaction for a customer visiting the store.
    report() -> str:
        Generates a daily report of customers and remaining stock.
    store_menu() -> None:
        Displays the main menu for store operations.
    """

    def __init__(self):
        self.stock = Stock()
        self.customers: List[Customer] = []
        self.stock.setup_store()


    def find_product(self, product_name: str) -> Product:
        """
        Finds and returns a product by its name.

        Parameters
        ----------
        product_name : str
            The name of the product to find.

        Returns
        -------
        Product
            The product with the specified name, or None if not found.
        """

        return self.stock.find_product(product_name)

    def add_customer(self, customer: Customer):
        """
        Adds a customer to the store.

        Parameters
        ----------
        customer : Customer
            The customer to be added to the store.
        """


        self.customers.append(customer)

    def customer_account(self) -> None:
        """
        Handles the interaction for a customer visiting the store.

        Prompts the user for their name and the products they wish to purchase,
        then generates a receipt for the customer.
        """
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        customer = Customer(first_name, last_name)
        self.add_customer(customer)

        while True:
            product_name = input("Enter the product name (or 'done' to finish): ")
            if product_name.lower() == 'done':
                break
            product = self.find_product(product_name)
            if product:
                quantity = float(input(f"Enter the quantity of {product_name} : "))
                customer.add_to_cart(product, quantity)
            else:
                print("Product not found")

        print(customer.receipt())

    def report(self) -> str:
        """
        Generates a daily report of customers and remaining stock.

        Returns
        -------
        str
            A formatted string containing the daily report.
        """

        report_lines = ["Daily Report:"]
        report_lines.append("Customers:")
        for customer in self.customers:
            report_lines.append(str(customer))
            report_lines.append("Remaining Stock:")
            report_lines.append(str(self.stock))
            return "\n".join(report_lines)

