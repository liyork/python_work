import matplotlib.pyplot as plt

# 折线图
if __name__ == '__main__':
    input_values = [1, 2, 3, 4, 5]
    squares = [1, 4, 9, 16, 25]

    # 查看样式, plt.style.available
    plt.style.use('seaborn')

    # fig整张图片，ax图片中的各个图表
    fig, ax = plt.subplots()  # 绘制点在图片上
    ax.plot(input_values, squares, linewidth=3)  # 绘制图表， linewidth线条粗细

    # 设置图表标题并给坐标轴加上标签
    ax.set_title("ping fang shu", fontsize=24)
    ax.set_xlabel("zhi", fontsize=14)
    ax.set_ylabel("zhi de ping fang", fontsize=14)

    # 设置刻度标记的大小
    ax.tick_params(axis='both', labelsize=14)

    plt.show()  # 打开查看器并显示
