from typing import Dict, List
from Product import Product
from Customer import Customer

class Store:
    def __init__(self):
        self.products: Dict[str, Product] = {}
        self.customers: List[Customer] = []

    def find_product(self, product_name: str) -> Product:
        return self.products.get(product_name)

    def add_customer(self, customer: Customer):
        self.customers.append(customer)

    def customer_account(self):
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
                quantity = float(input(f"Enter the quantity of {product_name} (in {product.unit}): "))
                customer.add_to_cart(product, quantity)
            else:
                print("Product not found")

        print(customer.receipt())

    def report(self) -> str:
        report_lines = ["Daily Report:"]
        report_lines.append("Customers:")
        for customer in self.customers:
            report_lines.append(str(customer))
        report_lines.append("Remaining Stock:")
        for product in self.products.values():
            report_lines.append(str(product))
        return "\n".join(report_lines)
