import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

l1 = 0.0734
# l1 = 0.0834
# l1 = 0.0934
b = 5.85
d = 0.00873
e = 0.66
l3 = 1.7

x3 = 10


def dx(t, x, y, z):
    return -l1 * x * math.log(x / y)


def dy(t, x, y, z):
    return b * x - d * x ** (2 / 3) * y - e * z * y


def dz(t, x, y, z):
    return -l3 * z


def RK4(t, x0, y0, z0, right, h):
    x_v = [x0]
    y_v = [y0]
    z_v = [z0]
    t_v = [t]
    x = x0
    y = y0
    z = z0
    while t <= right:
        a1 = h * dx(t, x, y, z)
        b1 = h * dy(t, x, y, z)
        c1 = h * dz(t, x, y, z)
        a2 = h * dx(t + h / 2, x + a1 / 2, y + b1 / 2, z + c1 / 2)
        b2 = h * dy(t + h / 2, x + a1 / 2, y + b1 / 2, z + c1 / 2)
        c2 = h * dz(t + h / 2, x + a1 / 2, y + b1 / 2, z + c1 / 2)
        a3 = h * dx(t + h / 2, x + a2 / 2, y + b2 / 2, z + c2 / 2)
        b3 = h * dy(t + h / 2, x + a2 / 2, y + b2 / 2, z + c2 / 2)
        c3 = h * dz(t + h / 2, x + a2 / 2, y + b2 / 2, z + c2 / 2)
        a4 = h * dx(t + h, x + a3, y + b3, z + c3)
        b4 = h * dy(t + h, x + a3, y + b3, z + c3)
        c4 = h * dy(t + h, x + a3, y + b3, z + c3)

        x += (a1 + 2 * a2 + 2 * a3 + a4) / 6
        y += (b1 + 2 * b2 + 2 * b3 + b4) / 6
        z += (c1 + 2 * c2 + 2 * c3 + c4) / 6

        t += h

        x_v.append(x)
        y_v.append(y)
        z_v.append(y)
        t_v.append(t)
        print(t)
    return [t_v, x_v, y_v, z_v]


values = RK4(0, 0.1, 0.1, 0.1, 150, 0.1)


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

name = 'l1={}(with treatment).png'.format(str(l1))
fig.savefig(name)

