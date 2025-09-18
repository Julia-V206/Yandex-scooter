# Юлия Владимирова, 34-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import data


def test_create_and_get_order():
    # 1. Создаём заказ
    response = sender_stand_request.post_new_order(data. ORDER_BODY)
    assert response.status_code == 201, f"Ошибка при создании заказа: {response.text}"

    # 2. Сохраняем номер трека
    track = response.json()["track"]

    # 3. Получаем заказ по треку
    response_get = sender_stand_request.get_order_by_track(track)
    assert response_get.status_code == 200, f"Ошибка при получении заказа: {response_get.text}"

    # 4. Проверяем, что трек совпадает
    assert response_get.json()["order"]["track"] == track