from pathlib import Path
import sys
import unittest

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))


from areashape.areashape import Circle, calculate_area

class CircleTestCase(unittest.TestCase):
    def test_circle_area(self):
        print('CircleTestCase')
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), 78.53981633974483)

    def test_circle_negative_radius(self):
        with self.assertRaises(TypeError):
            circle = Circle(-5)

    def test_circle_non_numeric_radius(self):
        with self.assertRaises(TypeError):
            circle = Circle('5')

if __name__ == '__main__':
    unittest.main()
