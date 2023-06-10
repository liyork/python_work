import matplotlib.pyplot as plt

# 绘制散点图
if __name__ == '__main__':
    x_values = range(1, 1001)
    y_values = [x ** 2 for x in x_values]
    print(y_values)

    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    # ax.scatter(2, 4, s=200)  # 绘制一个点, s表示点的尺寸
    # ax.scatter(x_values, y_values, c='red', s=10)
    # ax.scatter(x_values, y_values, c=(0, 0.8, 0), s=10)  # 红绿蓝
    ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)  # 颜色映射

    # 设置图表标题并给坐标轴加上标签
    ax.set_title("ping fang gen", fontsize=24)
    ax.set_xlabel("zhi", fontsize=14)
    ax.set_ylabel("zhi de pingfang", fontsize=14)

    # 设置刻度标记的大小
    ax.tick_params(axis='both', which='major', labelsize=14)

    # 设置每个坐标轴的取值范围, x和y的最小、最大值
    ax.axis([0, 1100, 0, 1100000])

    plt.show()
    # 保存
    # plt.savefig('squares_plot.png', bbox_inches='tight')
