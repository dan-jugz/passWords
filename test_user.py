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
        self.new_user= User("daniel","123abc")#create my user object
    
    def test_init(self):
        self.assertEqual(self.new_user.name,"daniel")
        self.assertEqual(self.new_user.password,"123abc")
        '''
        test to check if the object is initialised correctly
        '''

    def test_save_user(self):
        '''
        to check if the contact object is saved into
        '''
        self.new_user.save_user() #saving a user
        self.assertEqual(len(User.user_list),1)

        
if __name__=="__main__":
    unittest.main()
    