#!/usr/bin/env python

# -*- coding: utf-8 -*-

from typing import List

class Produit:
    def __init__(self, name: str, category: str, stock: float, price: float):
        self.name: str = name
        self.type: str = category
        self.stock: float = stock
        self.price: float = price

    def update_store(self, add_to_cart):
        self.stock -= add_to_cart

    def __str__(self):
        return f"product(name={self.name}, type={self.type}, stock={self.stock}, prix={self.price})"
