# Найти самый дорогой заказ на маркетплейсе
"""
Легенда:
Вы тестируете поиск на маркетплейсе. Пользователь отфильтровал товары по наличию ("В наличии").
Вам нужно убедиться, что система правильно определила максимальную цену среди доступных товаров.
"""

products = [
    {"name": "Mouse", "price": 50, "in_stock": True},
    {"name": "Monitor", "price": 1500, "in_stock": False}, # Самый дорогой, но его нет!
    {"name": "Laptop", "price": 1200, "in_stock": True},  # Наша цель
    {"name": "Keyboard", "price": 100, "in_stock": True},
]

# Логика: Найти самый дорогой товар, который есть в наличии
max_price = 0
for product in products:
    if product["in_stock"] == True:
        if product["price"] > max_price:
            max_price = product["price"]
print(max_price)


# Тест: Проверить, что максимальная цена среди товаров в наличии равна 1200 (ASSERT)
assert max_price == 1200

# Тест: Проверить, что максимальная цена среди товаров в наличии не равна 1500 (ASSERT)
assert max_price != 1500


print("Tests SUCCESS")