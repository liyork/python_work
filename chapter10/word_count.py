def count_word(filename):
    """计算一个文件中大致包含多少个单词"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        # print(f"sorry, the file {filename} doss not exist")
        pass  # 静默失败，然后继续
    else:
        words = contents.split()
        num_words = len(words)
        print(f"the file {filename} has about {num_words} words")


if __name__ == '__main__':
    filename = 'alice.txt'
    count_word(filename)

    filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txtr']
    for filename in filenames:
        count_word(filename)
