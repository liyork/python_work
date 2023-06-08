# import pizza  # 导入模块的全部
import pizza as p  # 用别名

if __name__ == '__main__':
    p.make_pizza(16, 'pepperni')
    p.make_pizza(12, 'mushrooms', 'green peppers')
