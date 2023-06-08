if __name__ == '__main__':
    squares = []
    for value in range(1, 11):
        square = value ** 2  # 乘方
        squares.append(square)
    print(squares)

    digits = range(0, 10)  # 可迭代对象(类型是对象)
    print(digits[1])
    print(min(digits))
    print(max(digits))
    print(sum(digits))

    # 列表解析
    # 定义      循环代码     for循环
    squares = [value ** 2 for value in range(1, 11)]
    print(squares)
