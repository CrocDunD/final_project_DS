from selenium.webdriver.common.by import By

user_name = (By.NAME,'user')
password = (By.ID,'current-password')
login_button = (By.XPATH,"//*[@class='css-3coq9d-button']")

class Login_Page:
    def __init__(self,driver):
        self.driver = driver

    def get_username_field(self):
        return self.driver.find_element(user_name[0],user_name[1])

    def get_password(self):
        return self.driver.find_element(password[0],password[1])

    def get_login_button(self):
        return self.driver.find_element(login_button[0],login_button[1])