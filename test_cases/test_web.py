import time

import allure
import pytest

from utilities.common_ops import get_data, By
from wokflows import web_flows
from wokflows.web_flows import Web_Flows as flow



@pytest.mark.usefixtures('init_web_driver')
class Test_Web:
    def teardown_method(self):
        flow.grafana_home()

    @allure.title('Verify Login Grafana')
    @allure.description('Test login to grafana')
    def test1_login(self):
        flow.login_flow(get_data('UserName'),get_data('Password'))
        flow.verify_grafana_title('Welcome to Grafana')

    @allure.title('Verify Login upper menu buttons')
    @allure.description('Check that the upper menu buttons exist')
    def test_verify_menu_btns(self):
        flow.verify_menu_btns_flow()

    @allure.title('Verify New User')
    @allure.description('Creates a new user')
    def test_verify_new_user(self):
        flow.open_users()
        flow.create_user('Dudsa','duda@di.com','Dudadi', 12345)
        flow.verify_number_of_users(3)

    @allure.title('Verify Delete User')
    @allure.description('Deletes a user')
    def test_verify_deleted_user(self):
        flow.open_users()
        flow.delete_user(By.USER, 'Dudsa')
        flow.verify_number_of_users(2)

    @allure.title('Verify Users Filters')
    @allure.description('Test the search bar in users page')
    @pytest.mark.parametrize('search_value,expected_users', web_flows.split_csv(web_flows.data))
    def test_csv(self,search_value,expected_users):
        flow.open_users()
        flow.search_user(search_value)
        flow.verify_number_of_users(int(expected_users))