def write():
    # w：写入模式，r：读取模式，a：附加模式，r+读写模式
    with open(filename, 'w') as file_object:
        file_object.write("i love progamming." + str(1) + "\n")  # 自动创建
        file_object.write("i love creating new games.\n")


def append():
    with open(filename, 'a') as file_object:
        file_object.write("i love progamming." + str(2) + "\n")
        file_object.write("i love creating new games2.\n")


if __name__ == '__main__':
    filename = 'programming.txt'

    # write()
    append()
