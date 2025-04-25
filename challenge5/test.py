import unittest
from challenge import count_baby_names
import os

class TestCountBabyNames(unittest.TestCase):
    def setUp(self):
        # Create a temporary file for testing
        self.test_file = 'test_babynames.txt'
        with open(self.test_file, 'w') as file:
            file.write("Alice\nBob\nAlice\nCharlie\nBob\nAlice\n")

    def tearDown(self):
        # Remove the temporary file after tests
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_count_baby_names(self):
        # Test the function with the temporary file
        expected_result = {'Alice': 3, 'Bob': 2, 'Charlie': 1}
        result = count_baby_names(self.test_file)
        self.assertEqual(result, expected_result)

    def test_file_not_found(self):
        # Test the function with a non-existent file
        result = count_baby_names('non_existent_file.txt')
        self.assertEqual(result, {})

if __name__ == '__main__':
    unittest.main()