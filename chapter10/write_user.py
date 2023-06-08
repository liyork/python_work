import json

if __name__ == '__main__':
    username = input("what is your name? ")

    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"we'll remember you when you come back, {username}")
