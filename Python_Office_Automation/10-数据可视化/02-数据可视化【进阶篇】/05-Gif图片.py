import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

plt.style.use('dark_background')

fig = plt.figure()
ax = plt.axes(xlim=(-50, 50), ylim=(-50, 50))
line, = ax.plot([], [], lw=2)


# 初始化函数
def init():
    # 创建空打印/帧
    line.set_data([], [])
    return line,


# 存储x轴和y轴点的列表
xdata, ydata = [], []


def ghostImage(x, y):
    xdata.append(x)
    ydata.append(y)
    if len(xdata) > 60:
        del xdata[0]
        del ydata[0]
    return xdata, ydata


def animate(i):
    t = i / 100.0
    x = 40 * np.sin(2 * 2 * np.pi * (t + 0.3))
    y = 40 * np.cos(3 * 2 * np.pi * t)

    # 将新点附加到x、y轴点列表
    line.set_data(ghostImage(x, y))
    return line,


# 绘图标题设置
plt.title('Creating a Lissajous figure with matplotlib')
# 隐藏轴细节
plt.axis('off')

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=400, interval=20, blit=True)
# 将动画另存为gif文件
anim.save('../source_material/02/05-Gif图片.gif', writer='imagemagick')
