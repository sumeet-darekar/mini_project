# menu.py
class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"{item} added to the menu.")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"{item} removed from the menu.")
        else:
            print(f"{item} is not in the menu!")

    def display_menu(self):
        print("\n--- Menu ---")
        for item in self.items:
            print(f" - {item}")
        print()
