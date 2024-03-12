from pathlib import Path
import sys
import unittest

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))


from areashape.areashape import Triangle, calculate_area

class TriangleTestCase(unittest.TestCase):
    def test_triangle_area(self):
        triangle = Triangle((0, 0), (4, 0), (0, 3))
        self.assertAlmostEqual(triangle.area(), 6.0)  

    def test_triangle_invalid_coords(self):
        with self.assertRaises(TypeError):
            triangle = Triangle((0, 0), (4, 'a'), (0, 3))

    def test_triangle_invalid_args(self):
        with self.assertRaises(TypeError):
            triangle = Triangle((0, 0), (4, 0))
            
    def test_right_angled_triangle(self):
        triangle = Triangle((0, 0), (3, 0), (0, 4))
        self.assertTrue(triangle.is_right_angled)

    def test_non_right_angled_triangle(self):
        triangle = Triangle((0, 0), (3, 0), (0, 3))
        self.assertFalse(triangle.is_right_angled)
        
    def test_area_by_sides(self):
        triangle = Triangle((0, 0), (3, 0), (0, 4))
        self.assertAlmostEqual(triangle.area_by_sides(3, 4, 5), triangle.area())

        triangle = Triangle((0, 0), (1, 0), (0, 1))
        self.assertAlmostEqual(triangle.area_by_sides(1, 1, 1), triangle.area())

if __name__ == '__main__':
    unittest.main()