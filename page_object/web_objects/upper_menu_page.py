from selenium.webdriver.common.by import By

general_btn = (By.CLASS_NAME, 'css-mgcb1x')
home_btn = (By.CLASS_NAME, 'css-alq3f2')
add_panel_btn = (By.XPATH, '//*[@aria-label="Add panel"]')
save_dashboard_btn = (By.XPATH, '//*[@aria-label="Save dashboard"]')
dashboard_settings_btn = (By.XPATH, '//*[@aria-label="Dashboard settings"]')
cycle_view_mode_btn = (By.XPATH, '//*[@aria-label="Cycle view mode"]')



class Upper_Menu_Page:
    def __init__(self,driver):
        self.driver = driver

    def get_general_btn(self):
        return self.driver.find_element(general_btn[0],general_btn[1])

    def get_home_btn(self):
        return self.driver.find_element(home_btn[0],home_btn[1])

    def get_add_panel_btn(self):
        return self.driver.find_element(add_panel_btn[0],add_panel_btn[1])

    def get_save_dashboard_btn(self):
        return self.driver.find_element(save_dashboard_btn[0],save_dashboard_btn[1])

    def get_dashboard_settings_btn(self):
        return self.driver.find_element(dashboard_settings_btn[0],dashboard_settings_btn[1])

    def get_cycle_view_mode_btn(self):
        return self.driver.find_element(cycle_view_mode_btn[0],cycle_view_mode_btn[1])