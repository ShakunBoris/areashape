from collections.abc import Iterable   
import math
import numpy as np

from .ABC import Shape


class Circle(Shape):
    ''' radius only accepted, no coordinates implementation '''
    def __init__(self, radius, coords = (0, 0)):
        if not isinstance(radius, (int, float)) or radius < 0:
            raise TypeError('Circle radius is int or float value >= 0')
        self.radius = radius
        self.coords = coords

    def area(self) -> float:
        return math.pi * self.radius ** 2
    


class Triangle(Shape):
    '''3 vertexes (x,y); side - vec; length as is'''
    def __init__(self, *args):
        if len(args) != 3:
            raise TypeError('triangle is 3 (x, y) vertexes. int V float')
        for a in args:
            if not isinstance(a, Iterable) or len(a)!=2 or \
                    not isinstance(a[0], (float, int)) or \
                        not isinstance(a[1], (float, int)):
                raise TypeError('must be ((x1,y1), (x2,y2), (x3,y3)) ONLY FLOAT OR INT')
        self.vertexes = [np.array(args[0]), np.array(args[1]), np.array(args[2])]
        self._sides = None
        self._lengths = None
        self._is_right_angled: bool = None
        # set rightaway
        self.update_attributes()
    
    def update_attributes(self):
        self._sides = [self.vertexes[1] - self.vertexes[0], self.vertexes[2] - self.vertexes[1], self.vertexes[0] - self.vertexes[2]] 
        self._lengths = [np.linalg.norm(self.sides[0]), np.linalg.norm(self.sides[1]), np.linalg.norm(self.sides[2])]
        self._is_right_angled = self.right_angled_check()
    
    @property
    def sides(self):
            return self._sides
    
    @property
    def lengths(self):
        return self._lengths
    
    @property
    def is_right_angled(self):
        return self._is_right_angled
    
    # not _hiding 
    def right_angled_check(self) -> bool:
        lengths = self.lengths.copy()
        lengths.sort()
        # NP can be useful, depends on how prescise we want ot be
        return lengths[0] ** 2 + lengths[1] ** 2 == lengths[2] ** 2
    
    def area(self) -> float:
        s = (self.lengths[0] + self.lengths[1] + self.lengths[2]) / 2
        return np.sqrt(s * (s - self.lengths[0]) * (s - self.lengths[1]) * (s - self.lengths[2]))
    
    @staticmethod
    def area_by_sides(*args):
        if len(args) != 3 or not all(isinstance(x, (int, float)) and x > 0 for x in args):
            raise TypeError('Must be 3 int or float > 0')
        l1, l2, l3 = args
        print(l1, l2, l3)
        s = (l1 + l2 + l3) / 2
        return np.sqrt(s * (s - l1) * (s - l2) * (s - l3))
    
    def __setattr__(self, name, value):
        if name in ['vertexes']:
            super().__setattr__(name, value)
            self.update_attributes()
        else:
            super().__setattr__(name, value)
            
    