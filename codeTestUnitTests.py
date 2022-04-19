"""
Author: Maciej Fec
Email: maciejfec1996@gmail.com

Test cases for the code test.
"""

from codeTest import multiples_of_a_until_x
import unittest

class TestCodeTest(unittest.TestCase):

    def test_a_until_x(self):
        """
        Tests if the function returns the correct values when a = a and x = x
        """

        a = 2
        x = 20
        expected = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
        result = multiples_of_a_until_x(a, x)

        self.assertEquals(expected, result)
    
    def test_a_plus_1_until_2x(self):
        """
        Tests if the function returns the correct values when a = a + 1 and x = x * 2
        """

        a = 2
        x = 20
        # Expected result when a = a + 1 and x = x * 2 (2 + 1 = 3, 20 * 2 = 40)
        expected = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39]
        result = multiples_of_a_until_x(a + 1, x * 2)

        self.assertEquals(expected, result)
    
    def test_a_plus_2_until_3x(self):
        """
        Tests if the function returns the correct values when a = a + 2 and x = x * 3
        """

        a = 2
        x = 20
        # Expected result when a = a + 2 and x = x * 3 (2 + 2 = 4, 20 * 3 = 60)
        expected = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60]
        result = multiples_of_a_until_x(a + 2, x * 3)

        self.assertEquals(expected, result)
    
    def test_a_until_x_when_a_is_0(self):
        a = 0
        x = 51

        expected = 0
        result = multiples_of_a_until_x(a, x)

        self.assertEquals(expected, result)
    
    def test_a_until_x_when_x_is_less_than_a(self):
        a = 9
        x = 6

        expected = -1
        result = multiples_of_a_until_x(a, x)

        self.assertEquals(expected, result)
    
    def test_a_until_x_when_a_is_a_float(self):
        a = 1.5
        x = 17

        expected = -1
        result = multiples_of_a_until_x(a, x)

        self.assertEquals(expected, result)
    
    def test_a_until_x_when_a_is_a_float(self):
        a = 3
        x = 20.9

        expected = -1
        result = multiples_of_a_until_x(a, x)

        self.assertEquals(expected, result)

if __name__ == "__main__":
    unittest.main()