if __name__ == '__main__':
    alien_0 = {'color': "green", 'points': 5}
    print(alien_0['color'])
    print(alien_0['points'])

    alien_0['x_position'] = 0
    alien_0['y_position'] = 25
    print(alien_0)

    alien_0['color'] = 'yellow'
    print(alien_0)

    del alien_0['points']
    print(alien_0)

    favorite_languages = {
        'jen': 'python',
        'sarash': 'c',
        'edward': 'ruby'
    }
    language = favorite_languages['sarash'].title()
    print(language)

    alien_0 = {'color': "green", 'speed': 'slow'}
    # 报错
    # print(alien_0['points'])
    # 没有时，默认值
    point_value = alien_0.get('points', 'no point value assigned')
    print(point_value)

    user_0 = {
        'username': 'efermi',
        'first': 'enrico',
        'last': 'fermi',
    }
    for key, value in user_0.items():
        print(f"\nkey: {key}")
        print(f"value: {value}")
