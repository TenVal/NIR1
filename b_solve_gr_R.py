import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# l1 = 0.0734
l1 = 0.0834
# l1 = 0.0934
b = 5.85
d = 0.00873
e = 0.66
l3 = 1.7


def dx(t, x, y):
    return -l1 * x * math.log(x / y)


def dy(t, x, y):
    return b * x - d * x ** (2 / 3) * y


def RK4(t, x0, y0, right, h):
    x_v = [x0]
    y_v = [y0]
    t_v = [t]
    x = x0
    y = y0
    while t <= right:
        a1 = h * dx(t, x, y)
        b1 = h * dy(t, x, y)
        a2 = h * dx(t + h / 2, x + a1 / 2, y + b1 / 2)
        b2 = h * dy(t + h / 2, x + a1 / 2, y + b1 / 2)
        a3 = h * dx(t + h / 2, x + a2 / 2, y + b2 / 2)
        b3 = h * dy(t + h / 2, x + a2 / 2, y + b2 / 2)
        a4 = h * dx(t + h, x + a3, y + b3)
        b4 = h * dy(t + h, x + a3, y + b3)

        x += (a1 + 2 * a2 + 2 * a3 + a4) / 6

        y += (b1 + 2 * b2 + 2 * b3 + b4) / 6
        t += h

        x_v.append(x)
        y_v.append(y)
        t_v.append(t)

    return [t_v, x_v, y_v]


values = RK4(0, 0.1, 0.1, 300, 0.1)


fig, ax = plt.subplots()

ax.plot(values[0], values[1], label="Объем раковых клеток")
ax.plot(values[0], values[2], label="Объем клеток эндотелия")
ax.set_xlabel("t, день")
ax.set_ylabel("x1, x2, mm^3")
ax.legend()
ax.grid()
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.plot(values[0], values[1], values[2], label='parametric curve')

plt.show()

name = 'l1={}(without treatment).png'.format(str(l1))
fig.savefig(name)

