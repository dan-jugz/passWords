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
        self.new_user=user("daniel","123abc")#create my user object
    
    def test_init(self):
        self.assertEqual(self.new_user.name,"dan")
        self.assertEqual(self.new_user.password,"123abc")
        '''
        test to check if the object is initialised correctly
        '''

