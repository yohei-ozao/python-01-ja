import unittest
from unittest import mock
from unittest.mock import patch
import io
import importlib


class TestFunction(unittest.TestCase):
    def test_convert(self):
        with unittest.mock.patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            importlib.import_module("convert", package=None)
            self.assertEqual(mock_stdout.getvalue(), "10.32\n")


if __name__ == "__main__":
    unittest.main()
