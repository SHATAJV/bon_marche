#!/usr/bin/env python

# -*- coding: utf-8 -*-

from typing import List


class Product:
    """
        A class to represent products.

Methods
    -------
    def update_store(self, quantity: float):
        Check if the quantity of the product is available.
    def total_price(self) -> float:
        Calculates the total price of the product listing in the cart.
    def receipt(self) -> str:
        Print a receipt of the cart with product, quantity, price and total price.
    """

    def __init__(self, name: str, category: str, stock: float, price: float):
        """
        Initialize product with their first and last name.
        :param name: str, name of product
        :param category: str, category
        :param stock: float, stock of products
        :param price: float, price of product
        """
        self.name: str = name
        self.category: str = category
        self.stock: float = stock
        self.price: float = price

    def update_store(self, quantity: float):
        """
        Check if the quantity of the product is available.
        :param quantity:
        :return:True or False
        """
        if self.stock >= quantity:
            self.stock -= quantity
            return True
        print("Insufficient stock ! Sorry")
        return False

    def __str__(self):
        """
        Print product name, category, stock, and price.
        :return: product name, category, stock, and price
        """
        return f"{self.name}, stock={self.stock}"
