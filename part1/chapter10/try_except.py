if __name__ == '__main__':
    try:
        print(5 / 0)
    except ZeroDivisionError:
        print("you can't divide by zero")
