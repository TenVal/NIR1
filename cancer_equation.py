import math


class CancerEquation(object):
    """Cancer Equation"""
    def __init__(self, l1=0.0834, b=5.85, d=0.00873, e=0.66, l3=1.7, u=0):
        self.l1 = l1
        self.b = b
        self.d = d
        self.e = e
        self.l3 = l3
        self.u = u

    def dx_r(self, t, x, y, z=0):
        """Equation for radius of cancer shaped sphere as a first approximation"""
        try:
            return -self.l1 * x * math.log(4 * math.pi * (x ** 3) / (3 * y)) / 3
        except ValueError:
            pass

    def dy_r(self, t, x, y, z=0):
        """Equation for volume of endothelium (cancer shaped sphere)"""
        return self.b * 4 * math.pi * (x ** 3) / 3 - self.d * ((4 * math.pi / 3) ** (2 / 3)) * (x ** 2) * y - self.e * z * y

    def dz(self, t, x, y, z=0):
        """Equation for inhibitor concentration"""
        return -self.l3 * z + self.u

    def dy(self, t, x, y, z=0):
        """Equation for volume of endothelium"""
        return self.b * x - self.d * x ** (2 / 3) * y - self.e * z * y

    def dx(self, t, x, y, z=0):
        """Equation for volume of cancer (free form)"""
        try:
            return -self.l1 * x * math.log(x / y)
        except ValueError:
            pass
