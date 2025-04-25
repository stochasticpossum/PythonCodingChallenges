import unittest
from datetime import datetime
from challenge import analyze_logs

class TestAnalyzeLogs(unittest.TestCase):
    def test_analyze_logs(self):
        expected_logs = [
            {'ip_address': '53.78.206.207', 'timestamp': '2011-03-23T00:00:00', 'http_method': 'PUT', 'url': '/contact', 'status_code': 200, 'user_agent': 'Mozilla/5.0'},
            {'ip_address': '53.103.33.130', 'timestamp': '2009-09-11T00:00:00', 'http_method': 'POST', 'url': '/contact', 'status_code': 404, 'user_agent': 'Safari/537.36'},
            {'ip_address': '233.96.79.113', 'timestamp': '2006-11-03T00:00:00', 'http_method': 'PUT', 'url': '/contact', 'status_code': 200, 'user_agent': 'Mozilla/5.0'},
            {'ip_address': '26.106.221.102', 'timestamp': '2000-07-17T00:00:00', 'http_method': 'DELETE', 'url': '/contact', 'status_code': 500, 'user_agent': 'Mozilla/5.0'},
            {'ip_address': '12.46.137.11', 'timestamp': '2011-07-26T00:00:00', 'http_method': 'GET', 'url': '/contact', 'status_code': 500, 'user_agent': 'Chrome/91.0.4472.124'},
            {'ip_address': '69.138.187.62', 'timestamp': '2010-09-25T00:00:00', 'http_method': 'DELETE', 'url': '/products', 'status_code': 404, 'user_agent': 'Chrome/91.0.4472.124'},
            {'ip_address': '14.161.35.223', 'timestamp': '2008-08-22T00:00:00', 'http_method': 'GET', 'url': '/home', 'status_code': 200, 'user_agent': 'Chrome/91.0.4472.124'},
            {'ip_address': '9.28.255.90', 'timestamp': '2013-08-28T00:00:00', 'http_method': 'POST', 'url': '/about', 'status_code': 500, 'user_agent': 'Safari/537.36'},
            {'ip_address': '108.91.145.121', 'timestamp': '2006-11-21T00:00:00', 'http_method': 'DELETE', 'url': '/contact', 'status_code': 500, 'user_agent': 'Chrome/91.0.4472.124'},
            {'ip_address': '123.207.119.150', 'timestamp': '2010-05-02T00:00:00', 'http_method': 'GET', 'url': '/products', 'status_code': 301, 'user_agent': 'Mozilla/5.0'},
            {'ip_address': '214.132.138.112', 'timestamp': '2003-03-25T00:00:00', 'http_method': 'GET', 'url': '/products', 'status_code': 500, 'user_agent': 'Mozilla/5.0'}
        ]
        actual_logs = analyze_logs()
        self.assertEqual(actual_logs, expected_logs)

if __name__ == '__main__':
    unittest.main()