if __name__ == '__main__':
    age = 19
    if age >= 18:
        print("you")
        print("have you ")
    else:
        print("sorr ")
        print("plesa ")

    age = 12

    if age < 4:
        price = 0
    elif age < 18:
        price = 25
    else:
        price = 40
    print(f"your cose si ${price}")

    requested_toppings = []
    # 判定是否为空
    if requested_toppings:
        requested_toppings.append("1")
    else:
        requested_toppings.append("2")
    print(requested_toppings)
