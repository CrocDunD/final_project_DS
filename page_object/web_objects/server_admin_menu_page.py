from selenium.webdriver.common.by import By


users_btn = (By.XPATH,'//div[6]/ul/li[2]/a')
orgs_btn = (By.XPATH,'//div[6]/ul/li[3]')
settings_btn = (By.XPATH,'//div[6]/ul/li[4]')
plugins_btn = (By.XPATH,'//div[6]/ul/li[5]')
stats_and_license_btn = (By.XPATH,'//div[6]/ul/li[6]')


class Server_Admin_Menu_Page:
    def __init__(self,driver):
        self.driver = driver

    def get_users_btn(self):
        return self.driver.find_element(users_btn[0], users_btn[1])

    def get_orgs_btn(self):
        return self.driver.find_element(orgs_btn[0], orgs_btn[1])

    def get_settings_btn(self):
        return self.driver.find_element(settings_btn[0], settings_btn[1])

    def get_plugins_btn(self):
        return self.driver.find_element(plugins_btn[0], plugins_btn[1])

    def get_stats_and_license_btn(self):
        return self.driver.find_element(stats_and_license_btn[0], stats_and_license_btn[1])