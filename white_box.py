import unittest


def is_of_age(years):
    if years >= 18:
        return True
    else:
        return False


class WhiteBoxTest(unittest.TestCase):
    
    def test_is_of_age(self):
        years = 20

        result = is_of_age(years)

        self.assertEqual(result, True)
    
    def test_is_a_minor(self):
        years = 15

        result = is_of_age(years)

        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
