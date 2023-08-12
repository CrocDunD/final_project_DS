from selenium.webdriver.common.by import By

search_field = (By.XPATH,'//*[@placeholder="Search user by login, email, or name."]')
new_user_btn = (By.CLASS_NAME,'css-1mhnkuh')
users_list = (By.XPATH,'//*/tbody/tr') #This is a list!
user_by_user_name =(By.XPATH,"//*[@title='name']")
delete_user = (By.XPATH,"//div[@class = 'page-container page-body']//span[text()[contains(.,'Delete user')]]")
confirm_delete_user = (By.XPATH,"//div[@class='css-gqsmf2']//span[text()[contains(.,'Delete user')]]")


class Server_Admin_Page:
    def __init__(self,driver):
        self.driver = driver

    def get_search_field(self):
        return self.driver.find_element(search_field[0], search_field[1])

    def get_new_user_btn(self):
        return self.driver.find_element(new_user_btn[0], new_user_btn[1])

    def get_users_list(self):
        return self.driver.find_elements(users_list[0], users_list[1])

    def get_delete_user(self):
        return self.driver.find_element(delete_user[0], delete_user[1])

    def get_confirm_delete_user(self):
        return self.driver.find_element(confirm_delete_user[0], confirm_delete_user[1])

    def get_users_by_index(self, index):
        return self.get_users_list()[index]

    def get_user_by_user_name(self, name):
        return self.driver.find_element(user_by_user_name[0],user_by_user_name[1].replace('name',str(name)))