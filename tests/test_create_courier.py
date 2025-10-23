import requests
import allure
from data import ResponseBody, Url

class TestCreateCourier:
    @allure.title('Test Successful new courier creation. Handle:/api/v1/courier')
    def test_creation_courier_success(self, generate_courier_data):
        registration = requests.post(url= f'{Url.MAIN_URL}{Url.CREATE_COURIER}', json=generate_courier_data[0])
        assert registration.status_code == 201 and (registration.json() == ResponseBody.COURIER_CREATION_SUCCESS)

    @allure.title('Test Registration of two Identical Couriers Error. Handle:/api/v1/courier')
    def test_creation_courier_clone_error(self, create_courier):
        response_status = requests.post(url= f'{Url.MAIN_URL}{Url.CREATE_COURIER}', json=create_courier[0])
        assert response_status.status_code == 409 and (response_status.json() == ResponseBody.COURIER_NAME_ALREADY_EXIST)

    @allure.title('Test Courier Registration Deficit Data Error, Not enough: Login. Handle:/api/v1/courier')
    def test_creation_courier_deficit_data_error_login(self, create_courier_no_login):
        response_status = requests.post(url= f'{Url.MAIN_URL}{Url.CREATE_COURIER}', json=create_courier_no_login)
        assert response_status.status_code == 400 and (response_status.json() == ResponseBody.COURIER_REGISTRATION_NOT_ENOUGH_DATA)

    @allure.title('Test Courier Registration Deficit Data Error, Not enough: Password. Handle:/api/v1/courier')
    def test_creation_courier_deficit_data_error_password(self, create_courier_no_password):
        response_status = requests.post(url= f'{Url.MAIN_URL}{Url.CREATE_COURIER}', json=create_courier_no_password)
        assert response_status.status_code == 400 and (response_status.json() == ResponseBody.COURIER_REGISTRATION_NOT_ENOUGH_DATA)