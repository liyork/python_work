if __name__ == '__main__':
    # with再不需要访问文件后将其关闭
    with open('pi_digits.txt') as file_object:
        contents = file_object.read()  # 读取全部内容
    print(contents.rstrip())  # 去除由于read达到文件末尾返回空字符串

    # 相对路径
    with open('../text_files/a.txt') as file_object:
        contents = file_object.read()  # 读取全部内容
    print(contents.rstrip())

    # 绝对路径
    with open('/part1/text_files/a.txt') as file_object:
        contents = file_object.read()
    print(contents.rstrip())

    # 逐行读取
    filename = 'pi_digits.txt'
    with open(filename) as file_object:
        for line in file_object:
            print(line.rstrip())  # 去除文件每行本身的换行

    with open(filename) as file_object:
        lines = file_object.readlines()

    for line in lines:
        print(line.rstrip())
