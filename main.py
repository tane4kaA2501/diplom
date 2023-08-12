import configuration
import requests
import data


# Функция создания нового заказа
def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=order_body)


order_response = post_new_order(data.order_body)
track = order_response.json()['track']


# Функция получения заказа по треку
def get_order_on_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.CREATE_TRACK_PATH + str(track))


track_response = get_order_on_track(track)


# Проверка, что код 200
def test_possitive_assert_code():
    assert track_response.status_code == 200