if __name__ == '__main__':
    cars = ['bmw', 'audi', 'toyota', 'subaru']
    # 改变原有列表
    cars.sort()
    print(cars)
    cars.sort(reverse=True)
    print(cars)

    #  不改变原有列表
    newCars = sorted(cars)
    print(f"not change for old list: {cars}")
    print(newCars)

    # 改变原有列表
    newCars.reverse()
    print(newCars)

    print(len(newCars))

    # 错误，以后都不执行
    print(cars[11])
    print(111111)
