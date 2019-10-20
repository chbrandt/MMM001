class Point(object):
    def __init__(self, x, y):
        # multiply/divide x,y by 1 to implicitly check (x,y) for numbers
        self.x = 1 * x / 1
        self.y = 1 * y / 1

    def __add__(self, other):
        """
        Return a new Point object C = Point_A + Point_B
        """
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Point(new_x, new_y)

    def __sub__(self, other):
        """
        Return a new Point object C = Point_A - Point_B
        """
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Point(new_x, new_y)

    def __mul__(self, num):
        """
        Return a new Point object C = Point_A * number
        """
        new_x = num * self.x
        new_y = num * self.y
        return Point(new_x, new_y)

    def __truediv__(self, num):
        """
        Return a new Point object C = Point_A / number
        """
        new_x = self.x / num
        new_y = self.y / num
        return Point(new_x, new_y)

    def __str__(self):
        return "({x},{y})".format(x=self.x, y=self.y)

    def __repr__(self):
        return "Point({x},{y})".format(x=self.x, y=self.y)
