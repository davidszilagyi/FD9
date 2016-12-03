import os
import time
import sys
import inquirer
from importlib.machinery import SourceFileLoader
main_path = os.path.dirname(os.path.abspath(__file__))
# data manager module
data_manager = SourceFileLoader("data_manager", main_path + "/data_manager.py").load_module()


def print_welcome(message="new user"):
    if message == "new user":
        print("Welcome " + message)
    else:
        print("Welcome back" + str(message))


def print_message(message):
    print("\033[92m", "The " + str(message) + " is completed!", "\033[0m")


def get_inputs(datas_name, title):
    inputs = []
    print(title)
    for elements in range(len(datas_name)):
        inputs.append(input(datas_name[elements]))
    return inputs


def print_main_menu(table, title):
    options = []
    for elements in table:
        options.append(elements)
    options.append("Exit")
    questions = [inquirer.List("menu", message=title, choices=options,)]
    answer = inquirer.prompt(questions)
    return answer["menu"]


def print_sub_menu(table, title):
    questions = [inquirer.List('menu', message=title, choices=options,)]
    answer = inquirer.prompt(questions)
    return answer["menu"]


def get_help():
    print("Show tasks:\nYou can see what tasks is created for the current user\n\n" +
          "Add:\nUnique id is created automatically for the task.\nPlease enter the name of the task." +
          "\nThen if is it started (0), half completed (1) or completed and pushed to git (2).\n" +
          "\033[1m" + "Also need the deadline (must be in date form (mm/dd/yy): 31/12/16" + "\033[0m\n\n" +
          "Update:\nYou will need to select the id of the task, then you can choose from these options:\n" +
          "started (0), half completed (1), completed and pushed to git (2).\n" +
          "\033[1m" + "Also need the deadline (must be in date form (mm/dd/yy): 31/12/16" + "\033[0m\n\n" +
          "Remove:\nYou will need to select the id of the task what you want to remove.\n" +
          "It will be added to trash by your user name and also to available tasks.\n\n"
          "Show available tasks:\nYou will see what tasks are available.\n\n" +
          "Take from available tasks:\nYou will need to select the id of the task than it will be add to your tasks\n")
    return_to_menu = input("Please enter any key from your keyboard to go back to the menu...")
    
