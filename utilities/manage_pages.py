import test_cases
from page_object.web_objects.left_menu_page import Left_Menu_Page
from page_object.web_objects.login_page import Login_Page
from page_object.web_objects.main_page import Main_Page
from page_object.web_objects.server_admin_menu_page import Server_Admin_Menu_Page
from page_object.web_objects.server_admin_new_user_page import Server_Admin_New_User_Page
from page_object.web_objects.server_admin_page import Server_Admin_Page
from page_object.web_objects.upper_menu_page import Upper_Menu_Page

web_login = None
web_main = None
web_upper_menu = None
web_server_admin_page = None
web_server_admin_menu_page = None
web_server_admin_new_user_page = None
web_left_menu_page = None


class Manage_Pages:
    @staticmethod
    def init_web_pages():
        global web_login, web_main, web_upper_menu, web_upper_menu_page,\
            web_server_admin_menu_page, web_server_admin_page, web_server_admin_new_user_page,\
            web_left_menu_page

        web_login = Login_Page(test_cases.conftest.driver)
        web_main = Main_Page(test_cases.conftest.driver)
        web_upper_menu = Upper_Menu_Page(test_cases.conftest.driver)
        web_server_admin_menu_page = Server_Admin_Menu_Page(test_cases.conftest.driver)
        web_server_admin_page = Server_Admin_Page(test_cases.conftest.driver)
        web_server_admin_new_user_page = Server_Admin_New_User_Page(test_cases.conftest.driver)
        web_left_menu_page = Left_Menu_Page(test_cases.conftest.driver)
