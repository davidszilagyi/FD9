import os
import time
import sys
import ui
import random
import string


def get_user_name():
    with open("to_do.txt", "r") as file:
        lines = file.readlines()
    user = ui.get_inputs(["Please enter your username: "], "")
    user_search = "user:" + user[0]
    for data in lines:
        if str(user_search) == str(data.strip()):
            ui.print_welcome(user[0])
            return user[0]
    ui.print_welcome("new user", user[0])
    while True:
        question = ui.get_inputs(["Is it correct (Y\\N)? "], "")
        if question[0].lower() == "y":
            new_user = user_search
            #write_out(user, user)
            return user[0]
        else:
            user = get_user_name()
            return user


def generate_random(table):
    id_length = 6
    char_set = {0: string.ascii_lowercase, 1: string.ascii_uppercase, 2: string.digits, 3: string.digits,
                4: string.ascii_uppercase, 5: string.ascii_lowercase}
    while True:
        generated = ''
        for char in range(id_length):
                generated += char_set[char][random.randint(0, len(char_set)-1)]
        generated += "#&"
        if generated not in table:
            return generated


def specification(data):
    count_char = 0
    for char in data:
        if char == ":":
            return count_char
        else:
            count_char += 1
    return count_char


def search_in_file(search, specific):
    with open("to_do.txt", "r") as file:
        lines = file.readlines()
    searched = []
    for data in lines:
        if data == search:
            searched.append(data.replace(specific, ""))
    return searched


def user_names():
    with open("to_do.txt", "r") as file:
        lines = file.readlines()
    user_list = []
    for data in lines:
        if data[0:5] == "user:":
            user_name = ""
            for char in range(5, len(data)-1):
                if data[char] != ":":
                    user_name += data[char]
                elif data[char] == ":":
                    break
            user_list.append(user_name)
    return user_list
