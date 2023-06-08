import json

if __name__ == '__main__':
    filename = 'numbers.json'
    with open(filename) as f:
        numbers = json.load(f)

    print(numbers)
