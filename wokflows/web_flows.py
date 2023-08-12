import time

import allure

from extensions.verifications import Verifications as ver
from page_object.web_objects import server_admin_page
from page_object.web_objects import left_menu_page
from page_object.web_objects.main_page import main_title
from page_object.web_objects import server_admin_menu_page
from page_object.web_objects.server_admin_page import users_list
from test_cases import conftest
from utilities import manage_pages as page
from extensions.ui_actions import Ui_Actions
from utilities.common_ops import wait, For, get_data, read_csv


class Web_Flows:

    @staticmethod
    @allure.step('Go to homepage')
    def grafana_home():
        conftest.driver.get(get_data('Url'))


    @staticmethod
    @allure.step('Login to grafna')
    def login_flow(user: str, password: str):
        Ui_Actions.update_text(page.web_login.get_username_field(), user)
        Ui_Actions.update_text(page.web_login.get_password(), password)
        Ui_Actions.click(page.web_login.get_login_button())

    @staticmethod
    @allure.step('veify grafana title')
    def verify_grafana_title(expected: str,):
        wait(For.ELEMENT_EXISTS, main_title)
        actual = page.web_main.get_page_title().text
        ver.verify_equals(actual,expected)

    @staticmethod
    @allure.step('verify menu buttons displayed')
    def verify_menu_btns_flow():
        elems = [page.web_upper_menu.get_add_panel_btn(),
                 page.web_upper_menu.get_save_dashboard_btn(),
                 page.web_upper_menu.get_dashboard_settings_btn(),
                 page.web_upper_menu.get_cycle_view_mode_btn()
                 ]
        ver.soft_assert(elems)

    @staticmethod
    @allure.step('Go to users page')
    def open_users():
        wait(For.ELEMENT_EXISTS,left_menu_page.server_admin_btn)
        side_admin_btn = page.web_left_menu_page.get_server_admin_btn()
        wait(For.ELEMENT_EXISTS,server_admin_menu_page.users_btn)
        admin_menu_users_btn = page.web_server_admin_menu_page.get_users_btn()
        Ui_Actions.mouse_hover(side_admin_btn, admin_menu_users_btn)

    @staticmethod
    @allure.step('create new user')
    def create_user(name, email, user, password):
        Ui_Actions.click(page.web_server_admin_page.get_new_user_btn())
        Ui_Actions.update_text(page.web_server_admin_new_user_page.get_name_fld(), name)
        Ui_Actions.update_text(page.web_server_admin_new_user_page.get_email_fld(), email)
        Ui_Actions.update_text(page.web_server_admin_new_user_page.get_username_fld(), user)
        Ui_Actions.update_text(page.web_server_admin_new_user_page.get_password_fld(), password)
        Ui_Actions.click(page.web_server_admin_new_user_page.get_create_user_btn())


    @staticmethod
    @allure.step('verify number of users')
    def verify_number_of_users(expected):
        if expected > 0:
            wait(For.ELEMENT_DISPLAYED,users_list)
            ver.verify_number_of_elements(page.web_server_admin_page.get_users_list(), expected)


    @staticmethod
    @allure.step('delete user')
    def delete_user(by, value):
        if by == 'user':
            Ui_Actions.click(page.web_server_admin_page.get_user_by_user_name(value))
            wait(For.ELEMENT_DISPLAYED, server_admin_page.delete_user)
            Ui_Actions.click(page.web_server_admin_page.get_delete_user())
            Ui_Actions.click(page.web_server_admin_page.get_confirm_delete_user())
        elif by == 'index':
            Ui_Actions.click(page.web_server_admin_page.get_users_by_index(value))
            wait(For.ELEMENT_DISPLAYED, server_admin_page.delete_user)
            Ui_Actions.click(page.web_server_admin_page.get_delete_user())
            Ui_Actions.click(page.web_server_admin_page.get_confirm_delete_user())

    @staticmethod
    @allure.step('search user')
    def search_user(search_value):
        Ui_Actions.clear(page.web_server_admin_page.get_search_field())
        Ui_Actions.update_text(page.web_server_admin_page.get_search_field(), search_value)

data = read_csv(get_data('CSV_Location'))
def split_csv(data):
    testdata = []
    for i in data:
        testdata.append((i[0],i[1]))
    return testdata
