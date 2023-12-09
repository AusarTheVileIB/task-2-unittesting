import unittest
from ..anagrams import processed_string, reverse_only_letters

# Class for successful tests
class TestAnagramsFunction_Typical(unittest.TestCase):

    # Pass only alpha symbols
    def test_pass_correct_value_alpha(self):
        self.assertEqual(processed_string('raffaello olleaffar', reverse_only_letters), 'olleaffar raffaello')

    # Pass only numbers
    def test_pass_correct_value_numeric(self):
        self.assertEqual(processed_string('18901 18901', reverse_only_letters), '18901 18901')

    # Pass string with alpha numeric symbols
    def test_pass_correct_value_alpha_numeric(self):
        self.assertEqual(processed_string('a8f19 f8a19', reverse_only_letters), 'f8a19 a8f19')

    # Pass string with 2 letters divided by space
    def test_pass_correct_value_one_alpha_symbol(self):
        self.assertEqual(processed_string("G G", reverse_only_letters), "G G")

    # Pass string with 29+ symbols
    def test_pass_correct_value_thirteen_symbols(self):
        self.assertEqual(processed_string("nUGIpr4nnIE7XdBfKhWOvFmGo1cYxm mxYcoG4mFvO7WhKfBdXEInnrp1IGUn", reverse_only_letters), "mxYcoG4mFvO7WhKfBdXEInnrp1IGUn nUGIpr4nnIE7XdBfKhWOvFmGo1cYxm")

    # Pass special + alpha symbols
    def test_pass_correct_value_special_plus_alpha_symbols(self):
        self.assertEqual(processed_string('DHb0iQ~$h"oZ+ Zoh0Qi~$b"HD+', reverse_only_letters), 'Zoh0Qi~$b"HD+ DHb0iQ~$h"oZ+')

    # Test function on idempotency
    def test_on_idempotency(self):
        first_call_result = processed_string('41ph41nD 41Dn41hp', reverse_only_letters)
        second_call_result = processed_string('41ph41nD 41Dn41hp', reverse_only_letters)

        self.assertEqual(first_call_result, '41Dn41hp 41ph41nD')
        self.assertEqual(second_call_result, '41Dn41hp 41ph41nD')

        self.assertEqual(first_call_result, second_call_result)


class TestAnagramsFunction_Atypical(unittest.TestCase):

    # Empty string
    def test_pass_empty_string(self):
        with self.assertRaises(ValueError):
            self.assertEqual(processed_string('', reverse_only_letters), '')

    # String with one space
    def test_pass_string_space(self):
        self.assertEqual(processed_string(' ', reverse_only_letters), ' ')

    # String with double spaces
    def test_pass_string_double_space(self):
        self.assertEqual(processed_string('  ', reverse_only_letters), '  ')

    # Both values are 'None'
    def test_pass_none_value(self):
        with self.assertRaises(TypeError):
            self.assertEqual(processed_string(None, reverse_only_letters), None)

    # Passing value: Wrong first argument (not a string)
    def test_pass_wrong_first_argument(self):
        with self.assertRaises(TypeError):
            self.assertEqual(processed_string(True, reverse_only_letters), True)

    # Passing value: Wrong second argument (not a function)
    def test_pass_wrong_second_argument(self):
        with self.assertRaises(TypeError):
            self.assertEqual(processed_string('S7r1ng', 'g7n1rS'), 'g7n1rS')

    # Pass more than expected arguments
    def test_pass_more_than_expected_args(self):
        with self.assertRaises(TypeError):
            self.assertEqual(processed_string('4Nsw3r 4rws3N', reverse_only_letters, "Third argument"), "Not equals")

    # Pass less than expected arguments
    def test_pass_less_than_expected_args(self):
        with self.assertRaises(TypeError):
            self.assertEqual(processed_string("First argument"), 'First argument')



if __name__ == "__main__":
    unittest.main()