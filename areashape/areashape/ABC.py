from abc import ABC, abstractmethod


class Shape(ABC):

    # any shape MUST HAVE AREA method. this is why. or verbosly return exception
    @abstractmethod
    def area(self):
        pass

# areashape.calulate_area(shape obj)
def calculate_area(shape):
    ''' takes 1 shape obj as argument '''
    if isinstance(shape, Shape) and shape.__class__ is not Shape:
        return shape.area()
    else:
        raise ValueError(f'Error: Not an subclass of Shape. Shapes are: {[x.__name__ for x in Shape.__subclasses__()]}')