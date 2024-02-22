import unittest

from main import unique_substrings


class TestUniqueSubstrings(unittest.TestCase):
    def test_unique_substrings(self):
        input_string = "abcd"
        expected_result = ["a", "ab", "abc", "abcd", "b", "bc", "bcd", "c", "cd", "d"]
        self.assertEqual(unique_substrings(input_string), expected_result)

        input_string = ""
        expected_result = []
        self.assertEqual(unique_substrings(input_string), expected_result)

        input_string = "a"
        expected_result = ["a"]
        self.assertEqual(unique_substrings(input_string), expected_result)


if __name__ == "__main__":
    unittest.main()
