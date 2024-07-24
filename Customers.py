#!/usr/bin/env python

# -*- coding: utf-8 -*-

from typing import List


class Customers:
    def __init__(self,first_name:str,last_name:str):
        self.first_name:str = first_name
        self.last_name: str = last_name
        self.cart:list = []
    def add_to_cart(self,product:str,quantity:float):
        if product.update_store(quantity):
            self.cart.append(product,quantity)
        else:
            print("Insufficient stock! Sorry")

    def total_price(self) -> float:
        total_price = sum(product.price * quantity for product, quantity in self.cart)
        return total_price


    def receipt(self) -> str:
        for product, quantity in self.cart:
            print(f"{product.name} : {quantity} :{product.price}")
        print(f"Total price :{self.total_price()}")
