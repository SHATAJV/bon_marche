from typing import List


from product import Product
from customer import Customer
from stock import Stock


class Store:
    def __init__(self):
        self.stock = Stock()
        self.customers: List[Customer] = []
        self.stock.setup_store()
        self.sales_made: bool = False
    def find_product(self, product_name: str) -> Product:
        return self.stock.find_product(product_name)
    def add_customer(self, customer: Customer):
        self.customers.append(customer)
        self.sales_made = True
    def customer_account(self) -> None:
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

    def report_initial_stock(self):
        report_lines = ["Initial Stock Report:"]
        for product in self.stock.products.values():
            report_lines.append(f"{product.name}: {product.initial_stock}")
        return "\n".join(report_lines)


