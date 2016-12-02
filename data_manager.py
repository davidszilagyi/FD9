import os
import ui
import common


def update(start=False):
    if start is False:
        os.system("git add to_do.csv")
        os.system("git commit -m 'csv file changed'")
        os.system("git pull https://github.com/davidszilagyi/FD9")
        os.system("git push https://github.com/davidszilagyi/FD9.git")
    else:
        os.system("git pull https://github.com/davidszilagyi/FD9")
        ui.print_message("database update")


def get_user_name(start=False):
    with open("to_do.csv", "r") as file:
        lines = file.readlines()
    if start is False:
        user = ui.get_inputs(["Please enter the new username: "], "")
        user = "user:" + user
        write_out(user, user)
    else:
        user = ui.get_inputs(["Please enter your username: "], "")
        user = "user:" + user
        for data in lines:
            if user == data:
                user = data
                ui.print_welcome(user)
            else:
                user = ui.get_inputs([ui.print_welcome() + "\nPlease enter your username: "], "")
                user = "user:" + user
                write_out(user, user)
    return user


def write_out(user, data_to_write):
    with open("to_do.csv", "a") as file:
        lines = file.readlines()
    current_line = 0
    for data in lines:
        current_line += 1
        if data == user:
            file.write(data.replace(data_to_write))
            update()
        else:
            file.write(data_to_write)
