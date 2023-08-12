from selenium.webdriver.common.by import By

name_fld = (By.ID, 'name-input')
email_fld = (By.ID, 'email-input')
username_fld = (By.ID, 'username-input')
password_fld = (By.ID, 'password-input')
create_user_btn = (By.CLASS_NAME, 'css-1mhnkuh')




class Server_Admin_New_User_Page:
    def __init__(self,driver):
        self.driver = driver

    def get_name_fld(self):
        return self.driver.find_element(name_fld[0],name_fld[1])

    def get_email_fld(self):
        return self.driver.find_element(email_fld[0],email_fld[1])

    def get_username_fld(self):
        return self.driver.find_element(username_fld[0],username_fld[1])

    def get_password_fld(self):
        return self.driver.find_element(password_fld[0],password_fld[1])

    def get_create_user_btn(self):
        return self.driver.find_element(create_user_btn[0],create_user_btn[1])