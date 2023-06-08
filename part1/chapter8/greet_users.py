def greet_users(names):
    for name in names:
        msg = f"hello, {name.title()}!"
        print(msg)


if __name__ == '__main__':
    usernames = ['hannah', 'tr', 'margot']
    greet_users(usernames)
