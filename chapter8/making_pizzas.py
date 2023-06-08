# import pizza  # 导入模块的全部
from chapter8 import pizza as p

if __name__ == '__main__':
    p.make_pizza(16, 'pepperni')
    p.make_pizza(12, 'mushrooms', 'green peppers')
