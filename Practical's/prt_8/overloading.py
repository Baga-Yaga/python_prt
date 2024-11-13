import math

class AreaCalculator:
    def area(self, length, width=None):
        if width is None:
            raise ValueError("Width must be provided for a rectangle.")
        return length * width

    def area_circle(self, radius):
        return 3.14 * (radius ** 2)

    def area_triangle(self, base, height):
        return 0.5 * base * height

    def area_var(self, *args):
        if len(args) == 2:
            return self.area(args[0], args[1])
        elif len(args) == 1:
            return self.area_circle(args[0])
        elif len(args) == 3:
            return self.area_triangle(args[0], args[1])
        else:
            raise ValueError("Invalid number of arguments.")

calculator = AreaCalculator()


print("Area of Rectangle:", calculator.area_var(5, 10))
print("Area of Circle ", calculator.area_var(7))
print("Area of Triangle :", calculator.area_var(6, 4, 0))
