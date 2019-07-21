import unittest 
from cred import Info


class TestCred(unittest.TestCase):
    def setUp(self):
        self.new_info=Info("fbpass","emailpass")

    def test_init(self):
        self.assertEqual(self.new_info.facebk_pass,"fbpass")
        self.assertEqual(self.new_info.email_pass,"emailpass")

    def test_save_info(self):
        '''
        test if user info is saved
        '''
        self.new_info.save_info()
        self.assertEqual(len(Info.info_list),1)

    def tearDown(self):
        Info.info_list = []

    def test_delete_info(self):
        self.new_info.save_info()
        test_info = Info("briansfb","briansem")
        test_info.save_info()
        test_info.delete_info()
        self.assertEqual(len(Info.info_list),1)

        

if __name__ == '__main__':
    unittest.main()