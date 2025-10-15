import requests
import allure
import generators
from data import ResponseBody, Url

class TestLoginCourier:

    @allure.title('Test successful courier login, with complete login data. Handle:/api/v1/courier/login')
    def test_successful_courier_login(self, create_courier):
        response = requests.post(f'{Url.MAIN_URL}{Url.COURIER_LOGIN}', json=create_courier[1])
        courier_id = response.json()
        assert response.status_code == 200 and courier_id != ''

    @allure.title('Test Courier Login with non registered account. Handle:/api/v1/courier/login')
    def test_unregistered_courier_login(self):
        login_data = {'login': generators.login_generator(), 'password': generators.password_generator()}
        response = requests.post(f'{Url.MAIN_URL}{Url.COURIER_LOGIN}', login_data)
        assert response.status_code == 404 and (response.json() == ResponseBody.COURIER_ACCOUNT_NOT_FOUND)

    @allure.title('Test Courier Login Deficit Data Error with empty password. Handle:/api/v1/courier/login')
    def test_courier_login_empty_password_error(self, create_courier):
        data_response = {'login': create_courier[2], 'password': ''}
        response = requests.post(f'{Url.MAIN_URL}{Url.COURIER_LOGIN}', json=data_response)
        assert response.status_code == 400 and (response.json() == ResponseBody.COURIER_LOGIN_NOT_ENOUGH_DATA)

    @allure.title('Test Courier Login Deficit Data Error with empty login. Handle:/api/v1/courier/login')
    def test_courier_login_empty_login_error(self, create_courier):
        data_response = {'login': '', 'password': create_courier[3]}
        response = requests.post(f'{Url.MAIN_URL}{Url.COURIER_LOGIN}', json=data_response)
        assert response.status_code == 400 and (response.json() == ResponseBody.COURIER_LOGIN_NOT_ENOUGH_DATA)