from part1.chapter8.pizza import *  # 导入所有函数

# 最佳做法： 要么只导入需要使用的函数，要么导入整个模块并使用句点表示法
if __name__ == '__main__':
    make_pizza(16, 'pepperni')
    make_pizza(12, 'mushrooms', 'green peppers')
