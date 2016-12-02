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


def start():
    user = data_manager.get_user_name(True)
    data_manager.update(True)
    module_name = "FD9's to do manager: "
    user_list = common.get_user_names()
    while True:
        menu = ui.print_main_menu(user_list, module_name)
        if menu["menu"] == "Add new user":
            pass
        elif menu["menu"] == "Exit":
            sys.exit()
        else:
            options = ["Show tasks", "Add", "Update", "Remove", "Show trash", "Move from trash", "Back to main menu"]
            while True:
                sub_menu = ui.print_sub_menu(options, menu["menu"])
                if sub_menu["menu"] == "Show tasks":
                    pass
                elif sub_menu["menu"] == "Add":
                    pass
                elif sub_menu["menu"] == "Update":
                    pass
                elif sub_menu["menu"] == "Remove":
                    pass
                elif sub_menu["menu"] == "Show trash":
                    pass
                elif sub_menu["menu"] == "Move from trash":
                    pass
                elif sub_menu["menu"] == "Back to main menu":
                    break


def main():
    start()

if __name__ == "__main__":
    main()
