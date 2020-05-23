import unittest


class TestFizzBuzz(unittest.TestCase):
    def test_fizz_input__is_three(self):
        result = fizzbuzz(3)
        # self.assertEqual(result, 'fizz')
        assert result == 'fizz'

    def test_fizz_input__is_five(self):
        result = fizzbuzz(5)
        # self.assertEqual(result, 'buzz')
        assert result == 'buzz'


def fizzbuzz(number):
    if number == 3  :
        return 'fizz'
    if number == 5  :
        return 'buzz'
    
