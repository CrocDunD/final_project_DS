from selenium.webdriver.common.by import By

home_btn = (By.XPATH,'//*[@aria-label="Home"]')
search_btn = (By.XPATH,'//*[@aria-label="Search dashboards"]')
create_btn = (By.XPATH,'//*[@aria-label="Create"]')
dashboard_btn = (By.XPATH,'//*[@aria-label="Dashboards"]')
explore_btn = (By.XPATH,'//*[@aria-label="Explore"]')
alerting_btn = (By.XPATH,'//*[@aria-label="Alerting"]')
settings_btn = (By.XPATH,'//*[@aria-label="Configuration"]')
server_admin_btn = (By.XPATH,'//*[@aria-label="Server Admin"]')
admin_btn = (By.XPATH,'//*[@aria-label="admin"]')
help_btn = (By.XPATH,'//*[@aria-label="Help"]')

class Left_Menu_Page:
    def __init__(self,driver):
        self.driver = driver

    def get_home_btn(self):
        return self.driver.find_element(home_btn[0], home_btn[1])

    def get_search_btn(self):
        return self.driver.find_element(search_btn[0], search_btn[1])

    def get_create_btn(self):
        return self.driver.find_element(create_btn[0], create_btn[1])

    def get_dashboard_btn(self):
        return self.driver.find_element(dashboard_btn[0], dashboard_btn[1])

    def get_explore_btn(self):
        return self.driver.find_element(explore_btn[0], explore_btn[1])

    def get_alerting_btn(self):
        return self.driver.find_element(alerting_btn[0], alerting_btn[1])

    def get_settings_btn(self):
        return self.driver.find_element(settings_btn[0], settings_btn[1])

    def get_server_admin_btn(self):
        return self.driver.find_element(server_admin_btn[0], server_admin_btn[1])

    def get_admin_btn(self):
        return self.driver.find_element(admin_btn[0], admin_btn[1])

    def get_help_btn(self):
        return self.driver.find_element(help_btn[0], help_btn[1])
