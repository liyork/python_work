if __name__ == '__main__':
    pizza = {
        'crust': 'thick',
        'toppings': ['mushrooms', 'extra cheese']
    }
    print(f"your ordered a {pizza['crust']}-crust pizza "
          "with the following toppings:")
    for topping in pizza['toppings']:
        print("\t" + topping)
