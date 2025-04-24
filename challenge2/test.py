import unittest
from challenge import test_https

class TestChallenge(unittest.TestCase):
    def test_test_https(self):
        port_list = [80, 443, 8080]
        target_host = "142.250.9.113"
        expected_result = [(80, True), (443, True), (8080, False)]
        self.assertEqual(test_https(port_list, target_host), expected_result)

if __name__ == '__main__':
    unittest.main()