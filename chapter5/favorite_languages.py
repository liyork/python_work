if __name__ == '__main__':
    favorite_languages = {
        'jen': 'python',
        'sarash': 'c',
        'edward': 'ruby',
        'phil': 'python',
    }
    for name, language in favorite_languages.items():
        print(f"{name.title()}'s favorite language is {language.title()}")

    print()

    for name in favorite_languages.keys():
        print(name.title())

    friends = ['phil', 'sarash']
    # 默认遍历键
    for name in favorite_languages:
        print(name.title())

        if name in friends:
            language = favorite_languages[name].title()
            print(f"\t{name.title()}, i see you love {language}")

    # keys返回列表
    if 'erin' not in favorite_languages.keys():
        print("erin, please take our pool")

    print()

    for name in sorted(favorite_languages.keys()):
        print(f"{name.title()}, tank you for taking the poll")

    for language in favorite_languages.values():
        print(language.title())

    print()

    for language in set(favorite_languages.values()):
        print(language.title())

    aliens = []
    for alien_number in range(3):
        new_alien = {'color': 'green', 'points': alien_number, 'speed': 'slow'}
        aliens.append(new_alien)
    for alien in aliens[:2]:
        print(alien)
