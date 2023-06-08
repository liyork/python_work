if __name__ == '__main__':
    print("give me two num, i'll divide them.")
    print("enter 'q' to quit.")

    while True:
        first_num = input("first number: ")
        if first_num == 'q':
            break
        second_num = input("second number: ")
        if second_num == 'q':
            break
        try:
            answer = int(first_num) / int(second_num)
        except ZeroDivisionError:
            print("you can't divide by 0")
        else:  # try成功执行
            print(answer)
