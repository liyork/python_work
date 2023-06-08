def build_profile(first, last, **user_info):  # **空字典
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


if __name__ == '__main__':
    user_profile = build_profile('albert', 'einstein',
                                 location='princeton',
                                 field='physics')
    print(user_profile)
