#                                      API закакзов
# У нас есть список заказов, каждый заказ представлен в виде словаря с полями "id", "price" и "status".
orders = [
    {"id": 101, "price": 500, "status": "delivered"},
    {"id": 102, "price": 1000, "status": "canceled"},
    {"id": 103, "price": 300, "status": "delivered"},
]

# Задача: Вычислить общую сумму всех доставленных заказов (ЛОГИКА)
total_sum = 0
for order in orders:
    if order["status"] == "delivered":
         total_sum += order["price"]

print(total_sum)


# Тест: Проверить, что общая сумма доставленных заказов равна 800 (ASSERT)
assert total_sum == 800

# Тест: Проверить, что общая сумма доставленных заказов не равна 1000 (ASSERT)
assert total_sum != 1000

# Если оба теста прошли успешно, то выводим сообщение об успехе.
print("Tests SUCCESS")
