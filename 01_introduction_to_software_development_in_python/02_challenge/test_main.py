import unittest
from main import *


class TestMathCalculations(unittest.TestCase):
    def test_sum_result(self):
        self.assertEqual(sum_result, 30)

    def test_product_result(self):
        self.assertEqual(product_result, 7.0)

    def test_division_result(self):
        self.assertAlmostEqual(division_result, 3.3333333333333335)

    def test_remainder_result(self):
        self.assertEqual(remainder_result, 1)

    def test_power_result(self):
        self.assertEqual(power_result, 8)

    def test_sqrt_result(self):
        self.assertEqual(sqrt_result, 5.0)

    def test_absolute_value(self):
        self.assertEqual(absolute_value, 10)

    def test_floor_division_result(self):
        self.assertEqual(floor_division_result, 3)

    def test_average_result(self):
        self.assertEqual(average_result, 20.0)

    def test_celsius_conversion(self):
        self.assertEqual(celsius, 37.0)

    def test_perimeter(self):
        self.assertEqual(perimeter, 16)

    def test_area_circle(self):
        self.assertAlmostEqual(area_circle, 78.53981633974483)

    def test_meters_per_second(self):
        self.assertAlmostEqual(meters_per_second, 27.77777777777778)

    def test_hypotenuse(self):
        self.assertEqual(hypotenuse, 5.0)

    def test_volume_sphere(self):
        self.assertAlmostEqual(volume_sphere, 523.5987755982989)


if __name__ == "__main__":
    unittest.main()
