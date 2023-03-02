import numpy as np
import math
import matplotlib.pyplot as plt

aM = 3.8
am = 0.28
b = 1
g = 1
C = 1


def dy(x, y):
    return y * (aM / (b + 3) - am / 3 - 2 * (y ** g) / ((g + 1) * (g + 2) * (g + 3)))


def f(x, C):
    A = aM / (b + 3) - am / 3
    D = 2 / ((g + 1)*(g + 2)*(g + 3))
    return A ** (1 / g) / ((C + D * math.exp(-A * g * x)) ** (1 / g))

print("1.1 = {}".format(f(1, 1)))
x = -20
y = 0
right = 20
h = 1000


def rk4(x0, y0, xn, n):
    y_v = [y0]
    x_v = [x0]
    # Calculating step size
    h = (xn - x0) / n

    print('\n--------SOLUTION--------')
    print('-------------------------')
    print('x0\ty0\tyn')
    print('-------------------------')
    for i in range(n):
        k1 = h * (dy(x0, y0))
        k2 = h * (dy((x0 + h / 2), (y0 + k1 / 2)))
        k3 = h * (dy((x0 + h / 2), (y0 + k2 / 2)))
        k4 = h * (dy((x0 + h), (y0 + k3)))
        k = (k1 + 2 * k2 + 2 * k3 + k4) / 6
        yn = y0 + k
        print('%.4f\t%.4f\t%.4f' % (x0, y0, yn))
        print('-------------------------')
        y0 = yn
        x0 = x0 + h
        x_v.append(x0)
        y_v.append(y0)

    return [x_v, y_v]


def v_f(x0, y0, right, h):
    y = [f(x0, C)]
    x = [x0]
    while yn <= right:
        yn = f(x0, C)
        y.append(yn)
        x0 += h
        x.append(x0)
    return [x, y]


values_solve = rk4(x, y, right, h)
values_func = rk4(x, y, right, h)

# plt.plot(values[0], values[1])
plt.plot(values_solve[0], values_solve[1], label='Решение РК')
plt.plot(values_func[0], values_func[1], label='Решение ан.')
plt.legend(title='Решения')
plt.title("Y(x)")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
print(values_func[1])
