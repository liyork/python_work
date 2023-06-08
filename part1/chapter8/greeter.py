# 函数
def greet_user(username):
    # 文档字符串
    """显示问候语"""
    print(f"hello, {username.title()}!")


if __name__ == '__main__':
    greet_user('jess')
