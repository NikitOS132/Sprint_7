import generators

class Url:
    MAIN_URL = 'http://qa-scooter.praktikum-services.ru/'
    CREATE_COURIER = 'api/v1/courier'
    COURIER_LOGIN = 'api/v1/courier/login'
    COURIER_DELETE = 'api/v1/courier/'
    CREATE_ORDER = 'api/v1/orders'
    GET_ORDER_LIST = 'api/v1/orders'
    ORDER_CANCEL = 'api/v1/orders/cancel?track='
    TRACK_ORDER = 'api/v1/orders/track?t='

class DataForOrder:
    order_data = {
        "firstName": "Yakov",
        "lastName": "Shustrov",
        "address": "Buzheninova 9",
        "metroStation": 3,
        "phone": "+79250015400",
        "rentTime": 3,
        "deliveryDate": "2024-10-15",
        "comment": "Come in"
    }
    scooter_color = [['BLACK'], ['BLUE'], (['BLACK'], ['BLUE']), ['']]

class DataForRegistration:
    reg_data = [
        {'login': generators.login_generator(), 'firstName': generators.name_generator()}
    ]
class ResponseBody:
    COURIER_CREATION_SUCCESS = {'ok': True}
    COURIER_NAME_ALREADY_EXIST = {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}
    COURIER_REGISTRATION_NOT_ENOUGH_DATA = {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}
    COURIER_ACCOUNT_NOT_FOUND = {'code': 404, 'message': 'Учетная запись не найдена'}
    COURIER_LOGIN_NOT_ENOUGH_DATA = {'code': 400, 'message': 'Недостаточно данных для входа'}

class Flags:
    SUCCESSFUL_ORDER_CREATION = 'track'
    SUCCESSFUL_GET_ORDER_LIST = 'orders'