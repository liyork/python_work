import json
import os

# 反复执行，可以不断：创建-欢迎-创建-欢迎
if __name__ == '__main__':
    filename = 'username1.json'
    isExist = False
    try:
        with open(filename) as f:
            username = json.load(f)
            isExist = True
    except FileNotFoundError:
        isExist = False
        username = input("what is your name? ")
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"we'll remember you when you come back, {username}")
    else:
        print(f"welcome back, {username}")

    if isExist:
        os.remove(filename)
