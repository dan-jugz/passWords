import unittest
from user import User
 
class TestUser(unittest.TestCase):
    '''
    test class that defines testcases for the user class behaviour
    Parent class that helps create test cases
    '''
    def setUp(self):
        '''setup method to run before each testcase
        '''
        self.new_user= User("daniel","njuguna@gmail.com")#create my user object
    
    def test_init(self):
        self.assertEqual(self.new_user.name,"daniel")
        self.assertEqual(self.new_user.e_mail,"njuguna@gmail.com")
        '''
        test to check if the object is initialised correctly
        '''

    def test_save_user(self):
        '''
        to check if the user object is saved into
        '''
        self.new_user.save_user() #saving a user
        self.assertEqual(len(User.user_list),1)
    
    def test_save_multple_user(self):
        '''
        test save multiple contacts to check if we can save multiple contact
        '''
        self.new_user.save_user()
        test_user = User("sunday","sunday@brian.com") # new user
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    
    def tearDown(self):
        '''
        method that clears the array after each test has ran
        '''
        User.user_list=[]
    
    def test_delete_user(self):
        self.new_user.save_user()
        test_data= User("juliet","julie@gmail.com")
        test_data.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_display_users(self):
        '''
        test to see if the users are getting displayed
        '''
        self.assertEqual(User.display_users(),User.user_list)

    def test_login_user(self):
        '''
        test to login a user
        '''
        self.new_user.save_user()
        test_user=User("daniel","123abc@gmail.com")
        test_user.save_user()
        logged_in=User.user_verified("daniel","123abc@gmail.com")

        self.assertTrue(logged_in)

if __name__=="__main__":
    unittest.main()
    