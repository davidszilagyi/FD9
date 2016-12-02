import os
import time
import sys
import ui


def specification(data):
    count_char = 0
    for char in data:
        if char == ":":
            return count_char
        else:
            count_char += 1
    return count_char


def search_in_file(search, specific):
    with open("to_do.csv", "r") as file:
        lines = file.readlines()
    searched = []
    for data in lines:
        if data == search:
            searched.append(data.replace(specific, ""))
    return searched


def get_user_names():
    with open("to_do.csv", "r") as file:
        lines = file.readlines()
    user_list = []
    for data in lines:
        if data[0:5] == "user:":
            user_list.append(data[6::])
    return user_list
