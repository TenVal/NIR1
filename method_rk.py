class RK(object):
    def __init__(self, type):
        self.type = type

    def RK4_2D(self, t, x0, y0, right, h, dx, dy):
        """Method Runge-Kutta for 2D case (3 variables)"""
        x_v = [x0]
        y_v = [y0]
        t_v = [t]
        x = x0
        y = y0
        while t <= right:
            try:
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
            except TypeError:
                pass
            t += h

            x_v.append(x)
            y_v.append(y)
            t_v.append(t)
        return [t_v, x_v, y_v]

    def RK4_3D(self, t, x0, y0, z0, right, h, dx, dy, dz):
        """Method Runge-Kutta for 3D case (4 variables)"""
        x_v = [x0]
        y_v = [y0]
        z_v = [z0]
        t_v = [t]
        x = x0
        y = y0
        z = z0
        while t <= right:
            try:
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
            except TypeError:
                pass
            t += h
            x_v.append(x)
            y_v.append(y)
            z_v.append(y)
            t_v.append(t)
            # print(t)
        return [t_v, x_v, y_v, z_v]
