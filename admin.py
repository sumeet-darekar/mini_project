# admin.py
from user import User

class Admin(User):
    def modify_menu(self, menu):
        while True:
            action = input("Do you want to 'add' or 'remove' an item from the menu? (or type 'done' to exit): ")
            if action == 'done':
                break
            item = input("Enter the item: ")

            if action == 'add':
                menu.add_item(item)
            elif action == 'remove':
                menu.remove_item(item)
            else:
                print("Invalid action. Please type 'add' or 'remove'.")
