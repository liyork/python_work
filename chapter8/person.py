def build_person(first_name, last_name, age=None):  # None表示变量没有值
    person = {'first': first_name, 'last': last_name}
    if age:  # None相当于false
        person['age'] = age
    return person


if __name__ == '__main__':
    musician = build_person('jimi', 'hendrix')
    print(musician)
    musician = build_person('jimi', 'hendrix', age=29)
    print(musician)
