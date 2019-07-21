import unittest 
from cred import Info


class CredTest(unittest.TestCase):
    def setUp(self):
        self.new_info=Info("fbpass","emailpass")

    def test_init(self):
        self.assertEqual(self.new_info.facebk_pass,"fbpass")
        self.assertEqual(self.new_info.email_pass,"emailpass")

