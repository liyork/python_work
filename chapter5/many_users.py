if __name__ == '__main__':
    users = {
        'aeinstein': {
            'first': 'albert',
            'last': 'einstein',
            'location': 'princeton',
        },
        'aeinstein1': {
            'first': 'albert1',
            'last': 'einstein1',
            'location': 'princeton1',
        },
    }

    for username, user_info in users.items():
        print(f"\nUsername: {username}")
        full_name = f"{user_info['first']} {user_info['last']}"
        location = user_info['location']

        print(f"\tFull name: {full_name.title()}")
        print(f"\tLocation: {location.title()}")
