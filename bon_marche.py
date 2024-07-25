#!/usr/bin/env python


# -*- coding: utf-8 -*-
from store import Store


def store_menu(setup: Store):
    while True:
        print("Welcome to the store!")
        print("1. Customer visit")
        print("2. Daily report")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            setup.customer_account()
        elif choice == '2':
            print(setup.report())
        elif choice == '3':
            break
        else:
            print("Invalid choice, please try again")


if __name__ == "__main__":
    store = Store()
    store_menu(store)
