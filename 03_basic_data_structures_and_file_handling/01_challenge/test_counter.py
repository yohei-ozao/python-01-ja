import unittest
from unittest import mock
from unittest.mock import patch
from io import StringIO
from counter import counter
import re


class TestFunction(unittest.TestCase):
    def test_print(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            counter()
            expected_output_pattern = re.compile(r"apple\s*:\s*2")
            self.assertRegex(fake_out.getvalue(), expected_output_pattern)

    def test_dict(self):
        occurrences = counter()
        self.assertIn("apple", occurrences)
        self.assertIn("orange", occurrences)
        self.assertIn("banana", occurrences)
        self.assertIn("grape", occurrences)
        self.assertIn("melon", occurrences)
        self.assertIn("strawberry", occurrences)
        self.assertIn("kiwi", occurrences)


if __name__ == "__main__":
    unittest.main()
