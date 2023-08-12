import allure
from selenium.webdriver.remote.webelement import WebElement
from smart_assertions import soft_assert, verify_expectations


class Verifications:
    @staticmethod
    @allure.step('Verify equal values')
    def verify_equals(actual, expected):
        assert actual == expected, 'verification Failed!'

    @staticmethod
    @allure.step('Verify element is displayed')
    def is_displayed(elem: WebElement):
        assert elem.is_displayed(), 'verification Failed!'

    @staticmethod
    def soft_displayed(elems):
        failed_elems = []
        for i in range(len(elems)):
            if not elems[i].is_displayed:
                failed_elems.append(elems[i].get_attribute('aria-label'))
        if len(failed_elems) > 0:
            for i in failed_elems:
                print('Soft Displayed Failed:' + str(i))
            raise AssertionError('Soft Displayed Error')

    @staticmethod
    @allure.step('Verify displayed elements using smart assertion')
    def soft_assert(elems):
        for i in range(len(elems)):
            soft_assert(elems[i].is_displayed)
        verify_expectations()

    @staticmethod
    @allure.step('Verify number of elements')
    def verify_number_of_elements(list, expected_result):
        assert len(list) == expected_result, 'Number of elements in list does not match the expected result. Expected:'+ str(expected_result) +'actual result:' + str(len(list))
