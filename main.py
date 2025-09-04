from store import Store
from products import Product

def start(store):
    while True:
        print("\nStore Menu:")
        print("-------------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")
        print("-------------")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print("\nProducts in store:")
            products = store.get_all_products()
            if not products:
                print("No active products available.")
            for idx, p in enumerate(products, start=1):
                print(f"{idx}. {p.name}, Price: ${p.price:.2f}, Quantity: {p.quantity}")

        elif choice == "2":
            total_quantity = store.get_total_quantity()
            print(f"\nTotal of {total_quantity} products in the store")

        elif choice == "3":
            print()
            shopping_list = []
            products = store.get_all_products()
            for idx, p in enumerate(products, start=1):
                print(f"{idx}. {p.name}, Price: ${p.price:.2f}, Quantity: {p.quantity}")
            print("\nWhen you want to finish, enter empty text")
            while True:
                product_name = input("Product name: ")
                if product_name.lower() == "":
                    break
                try:
                    quantity = int(input("Quantity: "))
                except ValueError:
                    print("Please enter a valid number.")
                    continue

                # Suche nach dem Produkt im Store
                product = next((p for p in store.products if p.name == product_name), None)
                if product is None:
                    print("Product not found.")
                    continue
                shopping_list.append((product, quantity))

            if shopping_list:
                total_price = store.order(shopping_list)
                print(f"\nTotal price of your order: ${total_price:.2f}")

        elif choice == "4":
            print("Thank you for visiting. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    store = Store()
    store.add_product(Product("Apple", 10.00, 100))
    store.add_product(Product("Banana", 5.00, 200))
    store.add_product(Product("Orange", 3.00, 300))
    store.add_product(Product("Pear", 2.00, 400))
    store.add_product(Product("Strawberry", 1.00, 500))
    store.add_product(Product("Mango", 0.50, 600))
    store.add_product(Product("Grape", 0.25, 700))
    store.add_product(Product("Raspberry", 0.10, 800))
    start(store)