import os
import ui
import common


def update(start=False):
    if start is False:
        os.system("git remote add fd9 https://github.com/davidszilagyi/FD9.git")
        os.system("git add to_do.txt")
        os.system("git commit -m 'database updated'")
        os.system("git pull fd9 master")
        os.system("git push fd9 master")
        ui.print_message("database update")
    else:
        os.system("git pull fd9 master")
        os.system("clear")


def write_out(user, data_to_write):
    with open("to_do.txt", "a") as file:
        lines = file.readlines()
    current_line = 0
    for data in lines:
        current_line += 1
        if data == user:
            file.write(data.replace(data_to_write))
            update()
        else:
            file.write(data_to_write)
