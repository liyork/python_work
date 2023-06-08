from name_function import get_formatted_name

if __name__ == '__main__':
    print("enter 'q' at any time to quit.")
    while True:
        first = input("please give me a first name: ")
        if first == 'q':
            break
        last = input("please give me a last name: ")
        if last == 'q':
            break

        formatted_name = get_formatted_name(first, last)
        print(f"neatly formatted name: {formatted_name}")
