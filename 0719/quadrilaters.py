"""
Write a Quadrilater class representing a geometric figure with 4 sides.
Define:
    - attributes
    - perimeter method
    - gt, lt, eq methods
Extend then the Quadrilater class to a rectangle class defining:
    - new attributes (if necessary)
    - area method
Finally extend Quadrilater to a Rhombus class.
"""


class Quadrilater(object):

    def __init__(self, a, b, c, d):
        """Quadrilater object

        each variable represent a side length.
        :param a: side a length
        :type a: int
        :param b: "" b ""
        :type b: int
        :param c: "" c ""
        :type c: int
        :param d: "" d ""
        :type d: int
        """
        self.sides = tuple(a, b, c, d)

    def perimeter(self):
        return sum(self.sides)


class Rectangle(Quadrilater):

    def __init__(self, a, b):
        """Rectangle object

        sides are equals in pairs
        :param a: side a length
        :type a: int
        :param b: "" b ""
        :type b: int
        """
        self.super().__init__(a, b, a, b)

    def area(self):
        return self.sides[0] * self.sides[1]


class Rhombus(Quadrilater):

    def __init__(self, a, diag):
        """Rhombus object

        all sides equals, one diag as free param
        :param a: side a length
        :type a: int
        :param diag: free diagonal
        :type diag: int
        """
        self.super().__init__(a * 4)
        self.d1 = diag

    @property
    def d2(self):
        return (self.sides[0] ** 2 - self.diag ** 2) ** .5 * 2

    def area(self):
        return (self.d1 * self.d2) / 2
