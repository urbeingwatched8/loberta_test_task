import requests

import unittest

class TestResponse(unittest.TestCase):
    def test_returns200(self):
        response = str(requests.get('http://localhost'))
        self.assertEqual(response, '<Response [200]>')
    def test_returnsmytestsite(self):
        response = requests.get('http://localhost')
        txtt=str(response.text)
        self.assertEqual(txtt, 'My Test Site')


if __name__ == '__main__':
    unittest.main()
