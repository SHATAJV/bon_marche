from typing import List
from product import Product
from customer import Customer
from stock import Stock


class Store:
    """
    A class to represent a store that manages stock, customers, and sales.

    Attributes
    ----------
    stock : Stock
        An instance of the Stock class managing the store's products.
    customers : List[Customer]
        A list of Customer objects representing the store's customers.
    sales_made : bool
        A flag indicating whether any sales have been made.

    Methods
    -------
    find_product(product_name: str) -> Product:
        Finds and returns a product by its name.
    add_customer(customer: Customer):
        Adds a customer to the store and sets the sales_made flag to True.
    customer_account() -> None:
        Handles the customer account creation process, including product selection and receipt generation.
    report() -> str:
        Generates a daily report of customers and the remaining stock.
    report_initial_stock() -> str:
        Generates a report of the initial stock for each product.
    """

    def __init__(self):
        """
        Initializes the Store with an empty stock, an empty list of customers, and sets up the store's stock.
        """
        self.stock = Stock()
        self.customers: List[Customer] = []
        self.stock.setup_store()
        self.sales_made: bool = False

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
            The product object if found, otherwise None.
        """
        return self.stock.find_product(product_name)

    def add_customer(self, customer: Customer):
        """
        Adds a customer to the store and sets the sales_made flag to True.

        Parameters
        ----------
        customer : Customer
            The customer object to add.
        """
        self.customers.append(customer)
        self.sales_made = True

    def customer_account(self) -> None:
        """
        Handles the customer account creation process, including product selection and receipt generation.
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
                quantity = float(input(f"Enter the quantity of {product_name} (in {product.category}): "))
                customer.add_to_cart(product, quantity)
            else:
                print("Product not found")
        print(customer.receipt())

    def report(self) -> str:
        """
        Generates a daily report of customers and the remaining stock.

        Returns
        -------
        str
            A formatted string report of the day's customers and remaining stock.
        """
        if not self.sales_made:
            return "You didn't make any sales yet."
        report_lines = ["Daily Report:", "Customers:"]
        for customer in self.customers:
            report_lines.append(str(customer))
        report_lines.append("Remaining Stock:")
        for product in self.stock.products.values():
            report_lines.append(
                f"{product.name}: Initial Stock: {product.initial_stock}, Current Stock: {product.stock}")
        return "\n".join(report_lines)

    def report_initial_stock(self) -> str:
        """
        Generates a report of the initial stock for each product.

        Returns
        -------
        str
            A formatted string report of the initial stock for each product.
        """
        report_lines = ["Initial Stock Report:"]
        for product in self.stock.products.values():
            report_lines.append(f"{product.name}: {product.initial_stock}")
        return "\n".join(report_lines)
