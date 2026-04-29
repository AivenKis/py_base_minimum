# 1 Данные (Тестовые наборы данных)

electronics = [
    {"name": "Mouse", "price": 50, "in_stock": True},
    {"name": "Laptop", "price": 1200, "in_stock": True},
    {"name": "Monitor", "price": 1500, "in_stock": False},
    {"name": "Keyboard", "price": 100, "in_stock": True},
    {"name": "Headphones", "price": 900, "in_stock": True},
    {"name": "Smartphone", "price": 800, "in_stock": False},
    {"name": "Tablet", "price": 400, "in_stock": True},
    {"name": "Smartwatch", "price": 1250, "in_stock": True},
    {"name": "Camera", "price": 1600, "in_stock": False}
]

books = [
    {"name": "Python Book", "price": 300, "in_stock": True},
    {"name": "Old Magazine", "price": 500, "in_stock": False},
    {"name": "Data Science Book", "price": 250, "in_stock": True},
    {"name": "Cooking Book", "price": 100, "in_stock": True},
    {"name": "History Book", "price": 200, "in_stock": False},
    {"name": "Fiction Book", "price": 1150, "in_stock": True},
    {"name": "Science Book", "price": 800, "in_stock": True},
    {"name": "Art Book", "price": 400, "in_stock": False},
    {"name": "Travel Book", "price": 350, "in_stock": True}

]

furniture = [
    {"name": "Sofa", "price": 2000, "in_stock": True},
    {"name": "Table", "price": 800, "in_stock": False},
    {"name": "Chair", "price": 150, "in_stock": True},
    {"name": "Bed", "price": 3000, "in_stock": True},
    {"name": "Wardrobe", "price": 2500, "in_stock": False},
    {"name": "Bookshelf", "price": 1200, "in_stock": True},
    {"name": "Desk", "price": 1800, "in_stock": True},
    {"name": "Dresser", "price": 2200, "in_stock": False},
    {"name": "Nightstand", "price": 500, "in_stock": True}
]

shoes = [
    {"name": "Sneakers", "price": 150, "in_stock": True},
    {"name": "Boots", "price": 300, "in_stock": False},
    {"name": "Sandals", "price": 80, "in_stock": True},
    {"name": "Heels", "price": 200, "in_stock": True},
    {"name": "Flats", "price": 120, "in_stock": False},
    {"name": "Loafers", "price": 250, "in_stock": True},
    {"name": "Running Shoes", "price": 180, "in_stock": True},
    {"name": "Dress Shoes", "price": 350, "in_stock": False},
    {"name": "Slippers", "price": 60, "in_stock": True}
]

# 2. Объявление функции с передачей параметра
def get_max_price_in_stock(items):
    max_price = 0
    for product in items:
        if product["in_stock"]:
            if product["price"] > max_price:
                max_price = product["price"]



    return max_price

# 3. Вызов функции с передачей аргумента и сохранение результата в переменную
max_elec = get_max_price_in_stock(electronics)
max_books = get_max_price_in_stock(books)
max_furniture = get_max_price_in_stock(furniture)
max_shoes = get_max_price_in_stock(shoes)


# 4. Проверка результата с помощью assert
print("Самая высокая цена в разделе 'Электроника': ", max_elec)
print("Самая высокая цена в разделе 'Книги': ", max_books)
print("Самая высокая цена в разделе 'Мебель': ", max_furniture)
print("Самая высокая цена в разделе 'Обувь': ", max_shoes)

assert max_elec == 1250
assert max_books == 1150
assert max_furniture == 3000
assert max_shoes == 250

print("All tests SUCCESS")
