# 📌 Условие:
# Дан список названий месяцев:
# months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]


# Напишите программу, которая:

#     Найдёт самый короткий месяц по количеству букв.
#     Напечатает его название и длину.
#     (Опционально) Если таких месяцев несколько — напечатайте все.
#
# 📌 Подсказка:
#
#     Используйте len(month)
#     Заведите переменные: min_length и shortest_month
#     Обновляйте их, если нашли месяц короче текущего минимума


months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь",
          "Декабрь"]

min_length = 100
shortest_months = []

for month in months:
    current_length = len(month)

    if current_length < min_length:
        min_length = current_length
        shortest_months = [month]
    elif current_length == min_length:
        shortest_months.append(month)

print(f"Самый короткий месяц: {shortest_months}")
print(f"Длина: {min_length} символов")
