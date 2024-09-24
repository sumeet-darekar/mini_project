# staff.py
from user import User

class Staff(User):
    def manage_order(self, order):
        print(f"{self.name} is managing order ID {order.order_id}.")
        while True:
            new_status = input("Update order status (Preparing/Served/Cancelled/Done): ")
            if new_status in ["Preparing", "Served", "Cancelled", "Done"]:
                order.update_status(new_status)
                break
            else:
                print("Invalid status. Please try again.")
