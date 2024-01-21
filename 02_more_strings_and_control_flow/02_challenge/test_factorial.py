import unittest
from unittest import mock
from unittest.mock import patch
import io
from factorial import compute_factorial


class TestFunction(unittest.TestCase):
    @patch("builtins.input", return_value="3")
    def test_compute_factorial(self, mock_inputs):
        res = compute_factorial()
        self.assertEqual(res, 6)

    @patch("builtins.input", return_value="0")
    def test_compute_factorial_zero(self, mock_inputs):
        res = compute_factorial()
        self.assertEqual(res, 1)


if __name__ == "__main__":
    unittest.main()
