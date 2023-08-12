import allure
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from utilities.common_ops import get_data, get_timestamp
from utilities.event_listener import EventListener
from utilities.manage_pages import Manage_Pages

driver = None
action = None
web_driver = get_data('Browser')


@pytest.fixture(scope='class')
def init_web_driver(request):
    global driver, action , edriver
    #edriver = get_web_driver()
    #driver = EventFiringWebDriver(edriver, EventListener())
    driver = get_web_driver()
    action = ActionChains(driver)
    driver.maximize_window()
    driver.implicitly_wait(int(get_data('WaitTime')))
    driver.get(get_data("Url"))
    request.cls.driver = driver
    request.cls.action = action

    Manage_Pages.init_web_pages()
    yield
    driver.quit()


def get_web_driver():
    if web_driver.lower() == 'chrome':
        driver = get_chrome()
    elif web_driver.lower() == 'firefox':
        driver = get_firefox()
    elif web_driver.lower() == 'edge':
        driver = get_edge()
    else:
        raise Exception('Wrong Input, Unrecognised Browser')
    return driver


def get_chrome():
    chrome_driver = webdriver.Chrome((ChromeDriverManager(version='114.0.5735.90').install()))
    return chrome_driver

def get_firefox():
    ff_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    return ff_driver

def get_edge():
    edge_driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    return edge_driver

#catch exceptions and errors
def pytest_exception_interact(node, call, report):
    if report.failed:
        if driver is not None: #if it is not none - this is an exception from API tests
            image = get_data('ScreenshotPath') + 'screen_' + str(get_timestamp()) + '.png'
            driver.get_screenshot_as_file(image)
            allure.attach.file(image, attachment_type=allure.attachment_type.PNG)