import json

if __name__ == '__main__':
    filename = 'username.json'

    with open(filename) as f:
        username = json.load(f)
        print(f"welcome back, {username}")
