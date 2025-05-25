import unittest
from main import celsius_to_fahrenheit

class TestCelsiusToFahrenheit(unittest.TestCase):

    def test_freezing_point(self):
        self.assertEqual(celsius_to_fahrenheit(0), 32.0)

    def test_boiling_point(self):
        self.assertEqual(celsius_to_fahrenheit(100), 212.0)

    def test_negative_celsius(self):
        self.assertEqual(celsius_to_fahrenheit(-10), 14.0)

    def test_body_temperature(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(37.77777777777778), 100.0)

if __name__ == '__main__':
    unittest.main()
