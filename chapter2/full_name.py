if __name__ == '__main__':
    first_name = "ada"
    last_name = "lovelace"
    full_name = f"{first_name} {last_name}"  # f(format)字符串，字符串中使用变量值
    print(full_name)
    print(f"Hello, {full_name.title()}")

    # 制表符
    print("\tpython")
    print("languages:\n\tPython\n\tC\n\tJavaScript")

#     删除尾部空白
    favorite_language = ' python '
    favorite_language=favorite_language.rstrip()
    # 前空白
    favorite_language=favorite_language.lstrip()
    # 前后空白
    favorite_language=favorite_language.strip()
    print(favorite_language)

