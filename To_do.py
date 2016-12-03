import os
import time
import sys
from importlib.machinery import SourceFileLoader
main_path = os.path.dirname(os.path.abspath(__file__))
# User interface module
ui = SourceFileLoader("ui", main_path + "/ui.py").load_module()
# data manager module
data_manager = SourceFileLoader("data_manager", main_path + "/data_manager.py").load_module()
# common module
common = SourceFileLoader("common", main_path + "/common.py").load_module()


def start(username):
    module_name = "FD9's to do manager: "
    main_options = ["User menu", "Add new user", "Add new task", "Show all available tasks", "Show all taken tasks",
                    "Exit"]
    menu = ui.print_main_menu(main_options, module_name)
    if menu == "User menu":
        user_menu(username)
    elif menu == "Add new user":
        pass
    elif menu == "Add new task":
        pass
    elif menu == "Show all available tasks":
        pass
    elif menu == "Show all taken tasks":
        pass
    elif menu == "Exit":
        sys.exit()


def user_menu(username):
    module_name = "User menu"
    sub_menu = ui.print_sub_menu(user_list, module_name)
    if sub_menu == "Show tasks":
        pass
    elif sub_menu == "Add":
        pass
    elif sub_menu == "Update":
        pass
    elif sub_menu == "Remove":
        pass
    elif sub_menu == "Show available tasks":
        pass
    elif sub_menu == "Take from available tasks":
        pass
    elif sub_menu == "Back to main menu":
        start(username)


def main():
    data_manager.update(True)
    user = data_manager.get_user_name(True)
    start(user)

if __name__ == "__main__":
    main()
