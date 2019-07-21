

class User:
    '''
    create a class that generates new instances of user
    '''
    def __init__(self,name,e_mail):
        self.name=name
        self.e_mail=e_mail
        '''
        init method that helps us define the user properties
        Args
            self.name:user name
            self.password:user password
        '''
    user_list=[]  #empty contact list

    def save_user(self):
        '''
        saves user info into user list
        ''' 
        User.user_list.append(self)

    def delete_user(self):
        '''
        removes user from the list
        '''
        User.user_list.remove(self)
    
    @classmethod
    def display_users(cls):
        '''

        '''
        return cls.user_list

    @classmethod
    def user_verified(cls,name,password):
        '''
        '''
        for user in cls.user_list:
            if user.name==name and user.password==password:
                return True
            return False

