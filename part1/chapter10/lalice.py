if __name__ == '__main__':
    filename = 'alice.txt'

    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"sorry, the file {filename} doss not exist")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"the file {filename} has about {num_words} words")
