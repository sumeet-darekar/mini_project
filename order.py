# order.py
class Order:
    order_counter = 0  # To track unique order IDs

    def __init__(self, customer, items):
        Order.order_counter += 1
        self.order_id = Order.order_counter
        self.customer = customer
        self.items = items
        self.status = "Pending"

    def view_order(self):
        print(f"\nOrder ID: {self.order_id}")
        print(f"Customer: {self.customer.name}")
        print("Items ordered:")
        for item in self.items:
            print(f" - {item}")
        print(f"Status: {self.status}\n")

    def update_status(self, new_status):
        self.status = new_status
        print(f"Order {self.order_id} status updated to: {self.status}\n")
