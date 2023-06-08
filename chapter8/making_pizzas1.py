# from pizza import make_pizza # 导入模块的特定函数
from chapter8.pizza import make_pizza as mp  # 用别名

if __name__ == '__main__':
    mp(16, 'pepperni')
    mp(12, 'mushrooms', 'green peppers')
