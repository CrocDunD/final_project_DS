from selenium.webdriver.common.by import By

main_title = (By.XPATH,"//*[@class='css-1aanzv4']")

class Main_Page:
    def __init__(self,driver):
        self.driver = driver

    def get_page_title(self):
        return self.driver.find_element(main_title[0],main_title[1])