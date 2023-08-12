import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from test_cases import conftest


class Ui_Actions:
    @staticmethod
    @allure.step('Click')
    def click(elem: WebElement):
        elem.click()

    @staticmethod
    @allure.step('Send keys')
    def update_text(elem: WebElement, value):
        elem.send_keys(value)

    @staticmethod
    @allure.step('Mouse hover')
    def mouse_hover(elem1: WebElement, elem2: WebElement):
        ActionChains(conftest.driver).move_to_element(elem1).move_to_element(elem2).click().perform()

    @staticmethod
    @allure.step('Right click')
    def right_click(elem: WebElement):
        ActionChains(conftest.driver).context_click(elem).perform()

    @staticmethod
    @allure.step('Drag and drop')
    def drag_and_drop(elem1: WebElement, elem2: WebElement):
        ActionChains(conftest.driver).drag_andDrop(elem1,elem2).perform()

    @staticmethod
    @allure.step('Clear text')
    def clear(elem: WebElement):
        elem.clear()