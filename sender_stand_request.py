import configuration
import requests
def post_new_order(order_body):
    """Создание нового заказа"""
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
        json=order_body
    )


def get_order_by_track(track_number):
    """Получение заказа по номеру трека"""
    return requests.get(
        configuration.URL_SERVICE + configuration.GET_ORDER_PATH,
        params={"t": track_number}
    )