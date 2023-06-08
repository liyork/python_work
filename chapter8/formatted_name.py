def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name: # 非空则true
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


if __name__ == '__main__':
    musician = get_formatted_name('jimi', 'hendrix')
    print(musician)
    musician = get_formatted_name('john', 'hooker', 'lee')
    print(musician)
