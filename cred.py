class Info:
    info_list=[]

    def __init__(self, facebk_pass, email_pass):
        self.facebk_pass=facebk_pass
        self.email_pass=email_pass


    def save_info(self):
        '''
        method to save credentials
        '''
        Info.info_list.append(self)

    def delete_info(self):
        '''
        method to delete credentials
        '''
        Info.info_list.remove(self)