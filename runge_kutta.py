import math
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Microsoft Yahei'

# 欧拉法
y = 2.
t = 0.
h = 0.01
euler = []
while t < 30.:
    euler.append(y)
    y += h*math.sin(t)
    t += h

# 4阶龙格库塔法
y_ = 2.
t = 0.
four_order = []
while t < 30.:
    four_order.append(y_)
    y_ = y_ + (h * (math.sin(t) + 2. * math.sin(t + h / 2.) + 2. * math.sin(t + h / 2.) + math.sin(t + h))) / 6.
    t += h

# 原式解析解
x = np.linspace(0., 30., 3000)
y__ = -np.cos(x) + 3

print('%30s %25s %20s' % ('欧拉法', '4阶龙格库塔法', '原式解析解'))
for _, (a, b, c) in enumerate(zip(euler, four_order, y__)):
    print('第 %d 迭代 t=%f %15f %25f %25f' % (_, _ * h, a, b, c))

fig, ax = plt.subplots(3, 1)
ax[0].plot(euler)
ax[0].set_title('欧拉法')
ax[1].plot(four_order, color='orchid')
ax[1].set_title('4阶龙格库塔法')
ax[2].plot(y__, color='orange')
ax[2].set_title('解析式精确解 $-cos(t) + 3$')
plt.show()
