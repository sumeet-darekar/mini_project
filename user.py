# user.py
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def view_menu(self, menu):
        print(f"{self.name} is viewing the menu:")
        menu.display_menu()
