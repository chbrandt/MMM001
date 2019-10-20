# Lesson-3

## Exercises

### Lambda function
* What is the expected result of the following code?
```python
>>> fs = []
>>> for i in range(5):
...     fs.append(lambda: i*2)
>>> [f() for f in fs]
```
* Run the code and check if the output is as expected.
* What is the problem of this code? Can you fix it? (see [here](https://stackoverflow.com/a/938493/687896))

#### Solution/discussion
The code snippet seems to creating 5 lambda functions to do
a simple `*2` multiplication over the current `i` counter: `0 1 2 3 4`; And the result should be: `0 2 4 6 8`.

When we run the code snippet we get as result `8 8 8 8 8`.
Which is not what we are looking for.

> Notice that `i` is defined in the current (global) environment -- `print(i)` --, that is the last value `i` assumed during the loop.
> Lesson learned: variables defined in the `for` loop will persist after the loop is finished.

Effectively, if we change the value of `i` (say to `-1`), running again the last line '`[f() for f in fs]`' will output `-2 -2 -2 -2 -2`.

That happens because of the memory scope used by Python and how it resolves symbols (_i.e._, variable).
For instance, "`i * 2`" is *not* being evaluated when the functions are defined, but when they run; Since the variable `i` is *not* defined in the `lambda` definition it will use the _global_  `i`.

To solve that -- _i.e._, to make the `lambda` function save the current values of `i` -- a copy of the value should be done to the local (Lambda) scope:
```python
fs = []
for i in range(5):
    fs.append(lambda j=i: j*2)
[f() for f in fs]
```


### Point Class

```python
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
```
