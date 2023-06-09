import config
import requests
import data

# функция создает новый заказ
def post_new_order(order_body):
    # При обращении к функции ей передают полный путь до документации, а так же параметры запроса
    return requests.post(config.URL_SERVICE + config.CREATE_ORDER_PATH, json=order_body)
# Переменной присваивается вызов функции
response = post_new_order(data.order_body)
# Сохранение  ответа на запрос о создании пользователя в формате json
response_json = response.json()
# Сохранение  в переменную параметра track
track = response_json["track"]
# Сохранение в  переменной словаря со значением track
track_param = {'t':track}


# функция показывает заказ по его трек-номеру
def get_order_by_track():
    # При обращении к функции ей передают полный путь до документации, а так же параметры запроса
    return requests.get(config.URL_SERVICE + config.GET_ORDER_WITH_TRACK_PATH, params=track_param)
# Переменной присваивается вызов функции
response_1 = get_order_by_track()


