#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List


class Customers:
    """
    A class to represent customers.

Methods
    -------
    def add_to_cart(self, product: str, quantity: float):
        Add product and quantity to the cart.
    def total_price(self) -> float:
        Calculates the total price of the product listing in the cart.
    def receipt(self) -> str:
        Print a receipt of the cart with product, quantity, price and total price.
    """

    def __init__(self, first_name: str, last_name: str):
        """
        Initialize customers with their first and last name.
        :param first_name: str, the first name of customer.
        :param last_name: str, the last name of customer.
        """
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.cart: list = []  # Create list of product in the cart.

    def add_to_cart(self, product: str, quantity: float):
        """
        Add product and quantity to the cart.
        :param product: str, product to add to cart.
        :param quantity: float, quantity of product to add to cart.
        :return: product and quantity.
        """
        if product.update_store(quantity):  # If quantity is available, the product
            self.cart.append(product, quantity)  # is added to the cart.
        else:
            print("Insufficient stock! sorry")

    def total_price(self) -> float:
        """
        Calculates the total price of the product listing in the cart.
        :return: Total product prices in the cart.
        """
        total_price = sum(product.price * quantity for product, quantity in self.cart)
        return total_price

    def receipt(self) -> str:
        """
        Print a receipt of the cart with product, quantity, price and total price.
        :return: receipt.
        """
        for product, quantity in self.cart:
            print(f"{product.name} : {quantity} :{product.price}")
        print(f"Total price :{self.total_price()}")
