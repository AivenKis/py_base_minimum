#                                       УРОК 3.2: Методы (Функции внутри класса)
#                                              Roadmap: Stage 2, Item 4 (OOP)
#                                                       Задание:
"""""
Возьмите ваш класс User из прошлого задания и добавьте в него "мозги" (методы).

1. Скопируйте ваш класс User.
2. Добавьте метод get_info(self). Он должен возвращать (return) красивую строку:
    "Пользователь [ИМЯ], Email: [ПОЧТА]"
    (Используйте f-строки: f"Текст {self.variable}").

3. Добавьте метод is_valid_email(self).
        Логика простая: если в self.email есть значок "@" — возвращаем True.
        Если нет — возвращаем False.
4. Сценарий проверки:
        Создайте юзера с правильной почтой.
        Создайте юзера с неправильной почтой (например, "admin.shop.com" без собаки).
        Проверьте методы через print и assert.
"""

class User:                                             # - создание класса User
    def __init__(self, username, email, age):           # - инициализация атрибутов класса
        self.username = username                        # - self - это ссылка на текущий объект, который будет создан при инициализации
        self.email = email
        self.age = age

    def get_info(self):                                 # - метод для получения информации о пользователе
        return f"Пользователь {self.username}, Email: {self.email}"

    def is_valid_email(self):                            # - метод для проверки валидности email
        return "@" in self.email

# - создание объектов класса User
victor = User("Victor", "victor@example.com", 25)
anna = User("Anna", "anna@test.ru", 17)
demian = User("Demian", "demi@test.ru", 15)
misha = User("Misha", "mishka@mail.com", 52)
admin = User("Admin", "admin-shop.com", 30)
vasya = User("Vasya", "_1", 30)

# - проверка методов через print и assert
print(victor.get_info())
print(misha.get_info())
print(anna.get_info())
print(demian.get_info())
print(admin.get_info())
print(vasya.get_info())

assert victor.is_valid_email()
assert anna.is_valid_email()
assert demian.is_valid_email()
assert misha.is_valid_email()
assert not admin.is_valid_email()
assert not vasya.is_valid_email()

print("Почта Виктора валидна: ", victor.is_valid_email())
print("Почта Анны валидна: ", anna.is_valid_email())
print("Почта Демина валидна: ", demian.is_valid_email())
print("Почта Миши валидна: ", misha.is_valid_email())
print("Почта Админа валидна: ", admin.is_valid_email())
print("Почта Васи валидна: ", vasya.is_valid_email())
