"""

class PointAtt:
    def __init__(self, x: int, y: int):
        self.x, self.y = x, y

    def __str__(self):
        return 'PointAtt({self.x}, {self.y})'.format(self=self)
"""
class MyClass:
    @classmethod
    def class_method(cls):
        return 'this is a class method'


my_class = MyClass()

