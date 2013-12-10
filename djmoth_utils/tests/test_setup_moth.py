import unittest
import requests

from djmoth_utils.utils.moth import get_moth_http


class TestSetupMoth(unittest.TestCase):
    def test_send_request(self):
        moth_root_url = get_moth_http()
        r = requests.get(moth_root_url)

        self.assertEqual(r.status_code, 200)
        self.assertIn('A set of vulnerable scripts', r.text)

