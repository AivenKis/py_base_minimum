                                  # Задача №1: "Фильтр и Логика"
active_adult_users = []
users_data = [
    {"id": 1, "name": "Alice", "age": 25, "is_active": True},
    {"id": 1.2, "name": "Sarah", "age": 40, "is_active": True},
    {"id": 2, "name": "Bob", "age": 16, "is_active": True},
    {"id": 3, "name": "Charlie", "age": 30, "is_active": False},
    {"id": 4, "name": "Dave", "age": 22, "is_active": True},
]

for u in users_data:
    if u ["age"] >=18 and u ["is_active"] == True:
        active_adult_users.append(u["name"])
print(active_adult_users)


                                    # Задача №2: "Первый тест (Assert)"
# Тест № 1
assert "Alice" in active_adult_users
assert "Bob" not in active_adult_users

print("All test SUCCESS")

