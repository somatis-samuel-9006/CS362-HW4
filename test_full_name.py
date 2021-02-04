import unittest
from unittest.mock import patch
import full_name

class TestFullName(unittest.TestCase):

    good_input1 = "Samuel"
    good_input2 = "Somatis"
    @patch('builtins.input', side_effect = [good_input1, good_input2])  ##side_effects are the inputs that will be passed as mock to the function

    def test_regular_name(self, mock_input1):
        result1 = full_name.full_name()
        self.assertEqual(result1, "Your full name is Samuel Somatis")
        self.assertNotEqual(result1, "Your full name is Bob Jones")
        self.assertNotEqual(result1, "Samuel Somatis")

    #In my interpretation of this program, names that contain non-letters should be allowed, in case a user actually decided that they want their name to be something like "1234$ 443@@"
    weird_input1 = "$$$"
    weird_input2 = "123"
    @patch('builtins.input', side_effect = [weird_input1, weird_input2])

    def test_weird_name(self, mock_input2):
        result2 = full_name.full_name()
        self.assertEqual(result2, "Your full name is $$$ 123")
        self.assertNotEqual(result2, "Your full name is Bob Jones")
        self.assertNotEqual(result2, "$$$ 123")

    good_input3 = "Samuel"
    empty_input = ""
    @patch('builtins.input', side_effect = [good_input3, empty_input])

    def test_empty_input(self, mock_input3):
        result3 = full_name.full_name()
        self.assertEqual(result3, "Full name cannot be generated as 1 or more names were not entered")
        self.assertNotEqual(result3, "Your full name is Samuel")

if __name__ == '__main__':
    unittest.main()