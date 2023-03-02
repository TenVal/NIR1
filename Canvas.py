from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from method_rk import RK
from cancer_equation import CancerEquation
import matplotlib.cbook as cbook
import matplotlib.pyplot as plt
import numpy as np


class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=5):
        fig = Figure(figsize=(width, height), dpi=90)
        self.axes = fig.add_subplot(111)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

        # self.plot()

    def plot(self, check, l1=0.0834, b=5.85, d=0.00873, e=0.66, l3=1.7, u=0, days=120):
        self.axes.clear()
        r_0 = 3.62783
        # ax = self.figure.add_subplot(111)
        equation = CancerEquation(l1=l1, b=b, d=d, e=e, l3=l3, u=u)
        if check:
            method = RK(3)
            values = method.RK4_3D(0, 200, 200, 0, days, 0.1, equation.dx, equation.dy, equation.dz)
            values_r = method.RK4_3D(0, r_0, r_0, 0, days, 0.1, equation.dx_r, equation.dy_r, equation.dz)

            self.axes.plot(values[0], values[1], label="Объем раковых клеток")
            self.axes.plot(values[0], values[2], label="Объем клеток эндотелия")
            self.axes.plot(values_r[0], values_r[1], label="R раковых клеток")
            name = 'l1={}, u={} (with treatment).png'.format(str(l1), str(u))
        else:
            method = RK(2)
            values = method.RK4_2D(0, 200, 200, days, 0.1, equation.dx, equation.dy)
            values_r = method.RK4_2D(0, r_0, r_0, days, 0.1, equation.dx_r, equation.dy_r)

            self.axes.plot(values[0], values[1], label="Объем раковых клеток")
            self.axes.plot(values[0], values[2], label="Объем клеток эндотелия")
            self.axes.plot(values_r[0], values_r[1], label="R раковых клеток")
            name = 'l1={}(without treatment).png'.format(str(l1))
        # labels = values[2][::2500]
        # print(labels, values[2])
        # self.axes.set_xticks(rotation=45)
        self.axes.set_xlabel("t, день")
        self.axes.set_ylabel("x1, x2, mm^3")
        self.axes.legend()
        self.axes.grid()
        self.draw()
        return [values[0], values[1], values[2], values_r[1]]
        # return [values[0], values[1], values[2]]

    def plot_sphere(self, r, x0=0, y0=0):
        self.axes.clear()
        # self.axes.set_xlim(-70, 70)
        # self.axes.set_ylim(-85, 85)
        with cbook.get_sample_data('brain.jpg') as image_file:
            image = plt.imread(image_file)
        self.axes.imshow(image, extent=[-75, 75, -90, 90])
        t = np.linspace(0, 2*np.pi, 100)
        x = x0 + r * np.cos(t)
        y = y0 + r * np.sin(t)

        self.axes.plot(x, y, color="red")
        # self.axes.set_xlabel("R, m")
        self.axes.set_title("R, m")
        self.axes.set_ylabel("R, m")
        self.axes.grid()
        self.draw()
