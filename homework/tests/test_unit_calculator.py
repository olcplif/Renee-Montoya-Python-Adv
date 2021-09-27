from unittest import TestCase
from functions_to_test import Calculator


class TestCalculator(TestCase):
    def test_add_001(self):
        self.assertEqual(Calculator.add(-1, 1), 0)
        self.assertEqual(Calculator.add('1', '1'), '11')
        self.assertNotEqual(Calculator.add(1, 0), 0)
        self.assertIsInstance(Calculator.add(1, 1), int)
        self.assertIsInstance(Calculator.add('1', '1'), str)
        with self.assertRaises(TypeError):
            Calculator.add('1', 1)

    def test_subtract_002(self):
        self.assertEqual(Calculator.subtract(1, 1), 0)
        self.assertNotEqual(Calculator.subtract(1, 0), 0)
        self.assertIsInstance(Calculator.subtract(1, 1), int)
        with self.assertRaises(TypeError):
            Calculator.subtract('1', 1)


if __name__ == '__main__':
    TestCalculator()
