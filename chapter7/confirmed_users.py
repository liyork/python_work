if __name__ == '__main__':
    unconfirmed_users = ['alias', 'brian', 'candace']
    confirmed_users = []

    # 为空时停止
    while unconfirmed_users:
        current_user = unconfirmed_users.pop()

        print(f"verifying user: {current_user.title()}")
        confirmed_users.append(current_user)

    print("\nthe following users have been confirmed:")
    for confirmed_user in confirmed_users:
        print(confirmed_user.title())
