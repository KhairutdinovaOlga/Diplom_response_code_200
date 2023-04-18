import sender_standart_request

def positive_assert():
    # В переменную order_by_track_response сохраняется результат запроса на получение заказа по трек-номеру:
    order_by_track_response = sender_standart_request.get_order_by_track()
    # Проверяется, что код ответа равен 200
    assert order_by_track_response.status_code == 200

# Тест 1. Код ответа на запрос получения заказа по треку равен 200
def test_order_by_track_response_status_code_200():
    positive_assert()
# Тест 1 PASSED
