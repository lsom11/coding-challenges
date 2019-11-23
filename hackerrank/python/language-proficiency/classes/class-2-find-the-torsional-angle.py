import math


class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, O):
        x = self.x - O.x
        y = self.y - O.y
        z = self.z - O.z
        return Points(x, y, z)

    def dot(self, O):
        x = self.x * O.x
        y = self.y * O.y
        z = self.z * O.z
        return x + y + z

    def cross(self, O):
        x = self.y * O.z - self.z * O.y
        y = self.z * O.x - self.x * O.z
        z = self.x * O.y - self.y * O.x
        return Points(x, y, z)

    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), .5)


if __name__ == '__main__':
