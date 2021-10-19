from math import pi, sqrt

class Parameters:
    def __init__(self, par):
        self.par = par
        self.fig = None

    def choose_figure(self, figure):
        self.fig = figure

    def area(self):
        result = self.fig.area(self.par)
        print(round(result, 2), type(round(result, 2)))
        return round(result, 2)

    def perimeter(self):
        result = self.fig.perimeter(self.par)
        print(round(result, 2), type(round(result, 2)))
        return round(result, 2)

    def volume(self):
        result = self.fig.volume(self.par)
        print(round(result, 2), type(round(result, 2)))
        return round(result, 2)


class Circle:
    def area(self, par):
        return pi*(par**2)

    def perimeter(self, par):
        return 2*pi*par

    def volume(self, par):
        return 0


class Triangle:
    def area(self, par):
        return sqrt(3) / 4 * par ** 2

    def perimeter(self, par):
        return par*3

    def volume(self, par):
        return 0


class Square:
    def area(self, par):
        return par ** 2

    def perimeter(self, par):
        return par*4

    def volume(self, par):
        return 0



class Pentagon:
    def area(self, par):
        return (1/4)*sqrt(5*(5+2*sqrt(5)))*(par**2)

    def perimeter(self, par):
        return par*5

    def volume(self, par):
        return 0


class Hexagon:
    def area(self, par):
        return (3*sqrt(3)*par**2)/2

    def perimeter(self, par):
        return par*6

    def volume(self, par):
        return 0


class Cube:
    def area(self, par):
        return par**2*6

    def perimeter(self, par):
        return par*12

    def volume(self, par):
        return par**3


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    figure = Parameters(10)

    figure.choose_figure(Circle())
    assert figure.area() == 314.16

    figure.choose_figure(Triangle())
    assert figure.perimeter() == 30

    figure.choose_figure(Square())
    assert figure.area() == 100

    figure.choose_figure(Pentagon())
    assert figure.perimeter() == 50

    figure.choose_figure(Hexagon())
    assert figure.perimeter() == 60

    figure.choose_figure(Cube())
    assert figure.volume() == 1000

    print("Coding complete? Let's try tests!")
