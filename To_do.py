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
    module_name = "FD9's to do manager"
    main_options = ["User menu", "Add new task", "Show all available tasks", "Show all taken tasks", "Show trash", 
                    "Exit"]
    menu = ui.print_main_menu(main_options, module_name)
    if menu == "User menu":
        user_menu(username)
    elif menu == "Add new task":
        pass
    elif menu == "Show all available tasks":
        pass
    elif menu == "Show all taken tasks":
        pass
    elif menu == "Show trash":
        pass
    elif menu == "Exit":
        sys.exit()


def user_menu(username):
    module_name = "User menu for " + str(username)
    user_menu = ["Show tasks", "Add a task", "Update a task", "Remove a task", "Show availabe tasks",
                 "Take one from availabe tasks", "Show trash", "Back to Main Menu"]
    sub_menu = ui.print_sub_menu(user_menu, module_name)
    if sub_menu == "Show tasks":
        pass
    elif sub_menu == "Add a task":
        pass
    elif sub_menu == "Update a task":
        pass
    elif sub_menu == "Remove a task":
        pass
    elif sub_menu == "Show available tasks":
        pass
    elif sub_menu == "Take one from available tasks":
        pass
    elif sub_menu == "Show trash":
        pass
    elif sub_menu == "Back to Main Menu":
        start(username)


def main():
    os.chdir(main_path)
    data_manager.update(True)
    user = common.get_user_name()
    start(user)

if __name__ == "__main__":
    main()
