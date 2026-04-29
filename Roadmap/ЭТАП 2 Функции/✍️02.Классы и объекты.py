#                                                       УРОК 3: Классы и объекты
#                                                   Давайте научимся создавать структуру
#                                                                   Задание:
""""

1. Напишите класс User (Пользователь).
2. У пользователя должны быть атрибуты:
        username (имя)
        email (почта)
        age (возраст)

3. Создайте (инициализируйте) трех пользователей:
        Victor, victor@example.com, 25 лет
        Anna, anna@test.ru, 17 лет
        Admin, admin@shop.com, 30 лет
4. Сложите этих трех пользователей в список users_list.
5. Challenge: Пройдитесь циклом for по этому списку и распечатайте email только тех пользователей, кто старше 18 лет.
"""
# Подсказка: теперь обращение идет через точку: user.age, а не user["age"].

class User:                                             # - создание класса User
    def __init__(self, username, email, age):           # - инициализация атрибутов класса
        self.username = username                        # - self - это ссылка на текущий объект, который будет создан при инициализации
        self.email = email
        self.age = age

# - создание объектов класса User
victor = User("Victor", "victor@example.com", 25)
anna = User("Anna", "anna@test.ru", 17)
demian = User("Demian", "demi@test.ru", 15)
misha = User("Misha", "mishka@mail.com", 52)
admin = User("Admin", "admin@shop.com", 30)

# - создание списка пользователей
users_list = [victor, anna, demian, misha, admin]

# - цикл for для печати email пользователей старше 18 лет
for user in users_list:
    if user.age >= 18:
        print(user.email)