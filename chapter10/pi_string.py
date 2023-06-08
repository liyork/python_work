if __name__ == '__main__':
    filename = 'pi_digits.txt'
    with open(filename) as file_object:
        lines = file_object.readlines()

    pi_string = ''
    for line in lines:
        pi_string += line.strip()

    print(pi_string)
    print(len(pi_string))

    # 字符串是否在里面
    print('29891' in pi_string)

    replace = pi_string.replace('29891', "1111111111111111111111")
    print(replace)
