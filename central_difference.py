import math
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Microsoft Yahei'
T = math.pi


def x(t):
    return 5. * np.sin(2 * math.pi * t / T)


def v(t):
    return 5. * 2 * math.pi * np.cos(2 * math.pi * t / T) / T


def a(t):
    return -5. * np.sin(2 * math.pi * t / T) * (2. * math.pi / T) ** 2


t = float(input('请输入时间 t:'))
h = 0.01
vt = (x(t + h / 2.) - x(t - h / 2.)) / h
at = (x(t + h) - 2 * x(t) + x(t - h)) / h ** 2
print('时间 t = %f 时的数值解速度为：%f，精确速度为：%f' % (t, vt, v(t)))
print('时间 t = %f 时的数值解加速度为：%f，精确加速度为：%f' % (t, at, a(t)))
duration = np.linspace(0., 100., 1000)
fig, ax = plt.subplots(3, 1)
ax[0].plot(duration, x(duration))
ax[0].set_title('位置-时间')
ax[1].plot(duration, v(duration))
ax[1].plot(t, vt, 'ro')
ax[1].set_title('速度-时间')
ax[2].plot(duration, a(duration), color='orange')
ax[2].plot(t, at, 'o')
ax[2].set_title('加速度-时间')
plt.show()
