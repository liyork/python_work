if __name__ == '__main__':
    car = 'bmw'
    print(car == 'bmw')

    car = 'Audi'
    # lower不影响原值
    print(car.lower() == 'audi')

    age_0 = 22
    age_1 = 18
    print(age_0 >= 21 and age_1 > 21)

    # 是否存在
    requested_toppings = ['mushrooms', 'onions', 'pineapple']
    print('mushrooms' in requested_toppings)
    print('mushrooms' not in requested_toppings)
