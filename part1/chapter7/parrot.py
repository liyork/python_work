if __name__ == '__main__':
    prompt = "tell me something, and i will repeat it back to you:"
    prompt += "\nenter 'quit' to end the program. "

    # 默认true，可进入while
    active = True
    while active:
        message = input(prompt)
        if message == 'quit':
            active = False
        else:
            print(message)
