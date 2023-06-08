def make_pizza(size, *toppings):  # 任意数量参数，封装到元组中，放到最后
    print(f"making a {size}-inch pizza with the following toppings:")
    # print(toppings)
    for topping in toppings:
        print(f"- {topping}")
