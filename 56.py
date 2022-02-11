# from abc import ABCMeta,abstractmethod
from abc import ABC,abstractmethod
class Shape(ABC): # or class Shape(metaclass=ABCMeta)
    @abstractmethod
    def printarea(self):
        return 0
class Rectangle(Shape):
    type="rectangle"
    sides=4
    def __init__(self) -> None:
        self.length=6
        self.breadth=7
    def printarea(self):
        return self.length*self.breadth
rect1=Rectangle()
print(rect1.printarea())
tryobj=Shape()