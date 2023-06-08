import json
import os


# 重构版本

def get_stored_username():
    filename = 'username1.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    username = input("what is your name? ")
    filename = 'username1.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    username = get_stored_username()
    if username:
        print(f"welcome back, {username}")
    else:
        username = get_new_username()
        print(f"we'll remember you when you come back, {username}")


if __name__ == '__main__':
    greet_user()
