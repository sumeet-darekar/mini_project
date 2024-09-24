# customer.py
from user import User
from order import Order

class Customer(User):
    def __init__(self, user_id, name, contact_number, email):
        super().__init__(user_id, name)
        self.contact_number = contact_number
        self.email = email

    def place_order(self, menu):
        print(f"{self.name}, please select items from the menu:")
        menu.display_menu()

        selected_items = []
        while True:
            item = input("Enter the item you want to order (or type 'done' to finish): ")
            if item == "done":
                break
            if item in menu.items:
                selected_items.append(item)
                print(f"{item} added to the order.")
            else:
                print(f"{item} is not on the menu.")

        if selected_items:
            order = Order(self, selected_items)
            print(f"Order placed with ID: {order.order_id}")
            return order
        else:
            print("No items were ordered.")
            return None
