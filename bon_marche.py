from store import Store


# -*- coding: utf-8 -*-
def store_menu(store: Store):
    while True:
        print("\nStore Menu")
        print("1. Show Initial Stock")
        print("2. Report")
        print("3. Customer Account")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            print(store.report_initial_stock())
        elif choice == '2':
            print(store.report())
            if not store.sales_made:
                print("1. View initial stock report")
                print("3. Exit")
                sub_choice = input("Enter your choice: ")
                if sub_choice == '1':
                    print(store.report_initial_stock())
                elif sub_choice == '3':
                    break
        elif choice == '3':
            store.customer_account()
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")
if __name__ == "__main__":
    store = Store()
    store_menu(store)