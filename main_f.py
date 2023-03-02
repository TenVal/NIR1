# import numpy as np
import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
from method_rk import RK
from cancer_equation import CancerEquation

answer_treatment = input("If without treatment (2), else - (3): ")
answer_r = input("If R (2), else (1): ")
l1 = float(input("Input l1: "))
equation = CancerEquation()
fig, ax = plt.subplots()

if answer_treatment == "2":
    method = RK(2)
    if answer_r == "1":
        # values = RK4_2D(0, 0.1, 0.1, 300, 0.1)
        values = method.RK4_2D(0, 0.1, 0.1, 300, 0.1, equation.dx, equation.dy)
        name = 'l1={}(without treatment).png'.format(str(l1))
        ax.plot(values[0], values[1], label="Объем раковых клеток")
        ax.plot(values[0], values[2], label="Объем клеток эндотелия")
    else:
        values = method.RK4_2D(0, 0.1, 0.1, 300, 0.1, equation.dx_r, equation.dy_r)
        name = 'l1={}(without treatment)_R.png'.format(str(l1))
        ax.plot(values[0], values[1], label="R раковых клеток")
        # ax.plot(values[0], values[2], label="Объем клеток эндотелия")
else:
    method = RK(3)
    if answer_r == "1":
        values = method.RK4_3D(0, 0.1, 0.1, 0.1, 300, 0.1, equation.dx, equation.dy, equation.dz)
        name = 'l1={}(with treatment).png'.format(str(l1))
        ax.plot(values[0], values[1], label="Объем раковых клеток")
        ax.plot(values[0], values[2], label="Объем клеток эндотелия")
    else:
        values = method.RK4_3D(0, 0.1, 0.1, 0.1, 300, 0.1, equation.dx_r, equation.dy_r, equation.dz)
        name = 'l1={}(with treatment)_R.png'.format(str(l1))
        ax.plot(values[0], values[1], label="R раковых клеток")
        ax.plot(values[0], values[2], label="Объем клеток эндотелия")

print(values[1][-1])

ax.set_xlabel("t, день")
ax.set_ylabel("x1, x2, mm^3")
ax.legend()
ax.grid()
# 17346.493641437846 16.058593376745385 153.36682315235618 3.3205828006747904
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.plot(values[0], values[1], values[2], label='parametric curve')
plt.show()
# fig.savefig(name)
