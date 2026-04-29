# ✍️ Задача F4: Пронумеровать элементы списка

# Дан список: cities = ["Москва", "Питер", "Новосибирск"]
# Напечатайте каждый город с номером, начиная с 1.

# 💡 Можно использовать range(len(...)) или enumerate() (если хотите усложнить)

cities = ["Москва", "Питер", "Новосибирск", "Томск"]

for i, city in enumerate(cities, start=1):
    print(i, city)
# или

for index, city in enumerate(cities, start=1):
    print(index, city)
