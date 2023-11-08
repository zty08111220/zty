import seaborn as sns
import matplotlib.pyplot as plt

# 折线图
def plot_line():
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    sns.lineplot(x=x, y=y)
    plt.title("折线图")
    plt.xlabel("X轴")
    plt.ylabel("Y轴")
    plt.show()

# 散点图
def plot_scatter():
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    sns.scatterplot(x=x, y=y)
    plt.title("散点图")
    plt.xlabel("X轴")
    plt.ylabel("Y轴")
    plt.show()

# 柱状图
def plot_bar():
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    sns.barplot(x=x, y=y)
    plt.title("柱状图")
    plt.xlabel("X轴")
    plt.ylabel("Y轴")
    plt.show()

# 在主函数中调用绘图函数
if __name__ == "__main__":
    plot_line()
    plot_scatter()
    plot_bar()
