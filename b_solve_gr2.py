# import numpy as np
# import math
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
#
# l1 = 0.0734
# # l1 = 0.0834
# # l1 = 0.0934
# b = 5.85
# d = 0.00873
# e = 0.66
# l3 = 1.7
#
#
# # def dx(t, x, y):
# #     return -l1 * x * math.log(x / y)
# #
# #
# # def dy(t, x, y):
# #     return b * x - d * x ** (2 / 3) * y
#
#
# def dx(t, x, y, z = 0):
#     return -l1 * x * math.log(x / y)
#
#
# def dy(t, x, y, z):
#     return b * x - d * x ** (2 / 3) * y
#
#
# def dz(t, x, y, z):
#     return -l3 * z
#
#
# def RK4_2D(t, x0, y0, right, h):
#     x_v = [x0]
#     y_v = [y0]
#     t_v = [t]
#     x = x0
#     y = y0
#     while t <= right:
#         a1 = h * dx(t, x, y)
#         b1 = h * dy(t, x, y)
#         a2 = h * dx(t + h / 2, x + a1 / 2, y + b1 / 2)
#         b2 = h * dy(t + h / 2, x + a1 / 2, y + b1 / 2)
#         a3 = h * dx(t + h / 2, x + a2 / 2, y + b2 / 2)
#         b3 = h * dy(t + h / 2, x + a2 / 2, y + b2 / 2)
#         a4 = h * dx(t + h, x + a3, y + b3)
#         b4 = h * dy(t + h, x + a3, y + b3)
#
#         x += (a1 + 2 * a2 + 2 * a3 + a4) / 6
#
#         y += (b1 + 2 * b2 + 2 * b3 + b4) / 6
#         t += h
#
#         x_v.append(x)
#         y_v.append(y)
#         t_v.append(t)
#
#     return [t_v, x_v, y_v]
#
#
# def RK4_3D(t, x0, y0, z0, right, h):
#     x_v = [x0]
#     y_v = [y0]
#     z_v = [z0]
#     t_v = [t]
#     x = x0
#     y = y0
#     z = z0
#     while t <= right:
#         a1 = h * dx(t, x, y, z)
#         b1 = h * dy(t, x, y, z)
#         c1 = h * dz(t, x, y, z)
#         a2 = h * dx(t + h / 2, x + a1 / 2, y + b1 / 2, z + c1 / 2)
#         b2 = h * dy(t + h / 2, x + a1 / 2, y + b1 / 2, z + c1 / 2)
#         c2 = h * dz(t + h / 2, x + a1 / 2, y + b1 / 2, z + c1 / 2)
#         a3 = h * dx(t + h / 2, x + a2 / 2, y + b2 / 2, z + c2 / 2)
#         b3 = h * dy(t + h / 2, x + a2 / 2, y + b2 / 2, z + c2 / 2)
#         c3 = h * dz(t + h / 2, x + a2 / 2, y + b2 / 2, z + c2 / 2)
#         a4 = h * dx(t + h, x + a3, y + b3, z + c3)
#         b4 = h * dy(t + h, x + a3, y + b3, z + c3)
#         c4 = h * dy(t + h, x + a3, y + b3, z + c3)
#
#         x += (a1 + 2 * a2 + 2 * a3 + a4) / 6
#         y += (b1 + 2 * b2 + 2 * b3 + b4) / 6
#         z += (c1 + 2 * c2 + 2 * c3 + c4) / 6
#
#         t += h
#
#         x_v.append(x)
#         y_v.append(y)
#         z_v.append(y)
#         t_v.append(t)
#         print(t)
#     return [t_v, x_v, y_v, z_v]
#
#
# answer_treatment = input("If with treatment (2), else - (1): ")
# answer_r = input("If R (1), else (2): ")
#
# if answer_treatment == "2":
#     if answer_r == "1":
#         values = RK4_2D(0, 200, 200, 120, 0.1)
#         name = 'l1={}(without treatment).png'.format(str(l1))
#     else:
#         pass
# else:
#     if answer_r == "1":
#         values = RK4_3D()
#         name = 'l1={}(with treatment).png'.format(str(l1))
#     else:
#         pass
#
# fig, ax = plt.subplots()
# ax.plot(values[0], values[1], label="Объем раковых клеток")
# ax.plot(values[0], values[2], label="Объем клеток эндотелия")
# ax.set_xlabel("t, день")
# ax.set_ylabel("x1, x2, mm^3")
# ax.legend()
# ax.grid()
# # fig = plt.figure()
# # ax = fig.add_subplot(111, projection='3d')
# # ax.plot(values[0], values[1], values[2], label='parametric curve')
# plt.show()
# fig.savefig(name)
#
from method_rk import RK
from cancer_equation import CancerEquation
import matplotlib.pyplot as plt
# import numpy as np
import matplotlib.pylab as pylab
params = {'legend.fontsize': 'x-large',
          'figure.figsize': (6, 4),
          'axes.labelsize': 'x-large',
          'axes.titlesize':'x-large',
          'xtick.labelsize':'x-large',
          'ytick.labelsize':'x-large'}
pylab.rcParams.update(params)
r_0 = 3.62783
fig = plt.figure()
axes = fig.add_subplot(111)

l1 = 0.0834
b = 5.85
d = 0.00873
e = 0.66
l3 = 1.7
u = 50
check = input("Chek - ")

days = 50
equation = CancerEquation(l1=l1, b=b, d=d, e=e, l3=l3, u=u)
if check == "1":
    method = RK(3)
    values = method.RK4_3D(0, 200, 200, 0, days, 0.1, equation.dx, equation.dy, equation.dz)
    values_r = method.RK4_3D(0, r_0, r_0, 0, days, 0.1, equation.dx_r, equation.dy_r, equation.dz)

    axes.plot(values[0], values[1], label="Объем раковых клеток")
    axes.plot(values[0], values[2], label="Объем клеток эндотелия")
    # axes.plot(values_r[0], values_r[1], label="R раковых клеток")
    name = 'l1={}, u={} Развитие болезни с лечением.png'.format(str(l1), str(u))
else:
    method = RK(2)
    values = method.RK4_2D(0, 200, 200, days, 0.1, equation.dx, equation.dy)
    values_r = method.RK4_2D(0, r_0, r_0, days, 0.1, equation.dx_r, equation.dy_r)

    # axes.plot(values[0], values[1], label="Объем раковых клеток")
    # axes.plot(values[0], values[2], label="Объем клеток эндотелия")
    axes.plot(values_r[0], values_r[1], label="R раковых клеток")
    name = 'l1={} Развитие болезни при отсутствии лечения.png'.format(str(l1))
# labels = values[2][::2500]
# print(labels, values[2])
# self.axes.set_xticks(rotation=45)
print(values_r[1][-1])
axes.set_xlabel("t, день")
# axes.set_ylabel("R, mm")
axes.set_ylabel("x, y, $\mathregular{mm^3}$")
# axes.set_title(name)
axes.legend()
axes.grid()
plt.show()
# 3.317124973246897 0.7391636991007549