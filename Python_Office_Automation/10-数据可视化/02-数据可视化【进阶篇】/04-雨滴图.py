import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 确定再现性的随机状态
np.random.seed(19680801)

# 创建新图形和填充它的轴
fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1], frameon=False)
ax.set_xlim(0, 1), ax.set_xticks([])
ax.set_ylim(0, 1), ax.set_yticks([])

# 创建雨水数据
n_drops = 50
rain_drops = np.zeros(n_drops, dtype=[('position', float, 2),
                                      ('size',     float, 1),
                                      ('growth',   float, 1),
                                      ('color',    float, 4)])

# 在随机位置初始化雨滴
# 随机增长率
rain_drops['position'] = np.random.uniform(0, 1, (n_drops, 2))
rain_drops['growth'] = np.random.uniform(50, 200, n_drops)

# 构建我们将在动画期间更新的散射
# 随雨滴发展
scat = ax.scatter(rain_drops['position'][:, 0], rain_drops['position'][:, 1],
                  s=rain_drops['size'], lw=0.5, edgecolors=rain_drops['color'],
                  facecolors='none')


def update(frame_number):
    # 得到一个索引，我们可以用来重新生成雨滴。
    current_index = frame_number % n_drops

    # 随着时间的推移，使所有颜色更加透明。
    rain_drops['color'][:, 3] -= 1.0/len(rain_drops)
    rain_drops['color'][:, 3] = np.clip(rain_drops['color'][:, 3], 0, 1)

    # 把所有的圆圈变大
    rain_drops['size'] += rain_drops['growth']

    # 为雨滴选择一个新的位置，重置其大小
    # 颜色
    rain_drops['position'][current_index] = np.random.uniform(0, 1, 2)
    rain_drops['size'][current_index] = 5
    rain_drops['color'][current_index] = (0, 0, 0, 1)
    rain_drops['growth'][current_index] = np.random.uniform(50, 200)

    # 使用新的颜色、大小和位置更新散布集合
    scat.set_edgecolors(rain_drops['color'])
    scat.set_sizes(rain_drops['size'])
    scat.set_offsets(rain_drops['position'])


# 构造动画，使用更新函数作为动画
animation = FuncAnimation(fig, update, interval=10)
plt.show()
