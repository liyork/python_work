if __name__ == '__main__':
    motrocycles = ['honda', 'yamaha', 'suzuki']
    print(motrocycles)
    motrocycles[0] = 'ducati'
    print(motrocycles)

    motrocycles.append('ducati')
    print(motrocycles)

    # 插入0位置，包含当前及以后元素都向右移动
    motrocycles.insert(0, 'ducati1')
    print(motrocycles)

    # 用索引删除
    del motrocycles[0]
    print(motrocycles)

    # 从最后弹出
    popped_motorcycle = motrocycles.pop()
    print(motrocycles)
    print(popped_motorcycle)
    # 从位置弹出
    first_owned = motrocycles.pop(0)
    print(motrocycles)
    print(first_owned)

    # 只删除第一个出现的
    motrocycles.remove('yamaha')
    print(motrocycles)

