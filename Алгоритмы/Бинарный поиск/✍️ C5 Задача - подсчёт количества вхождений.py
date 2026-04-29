# ✍️ C5 Задача - подсчёт количества вхождений

# Используя функции binary_search_first и binary_search_last, напишите функцию count_occurrences(arr, target),
# которая возвращает, сколько раз число встречается в списке. Если элемент не найден — вернуть 0.

# 📌 Формула:
# количество = last_index - first_index + 1


# 🧠 Главная идея — гениально простая:
#
#     Если список отсортирован, то все вхождения одного и того же числа идут подряд.
#
# 👉 Значит, чтобы посчитать количество — достаточно найти:
#
#     Индекс первого вхождения → first
#     Индекс последнего вхождения → last


def binary_search_first(arr, target):
    low = 0
    high = len(arr) - 1
    steps = 0
    result = -1

    while low <= high:
        steps += 1
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == target:
            result = mid
            high = mid - 1  # Продолжаем поиск влево для первого вхождения

        elif guess < target:
            low = mid + 1

        else:
            high = mid - 1

    return result, steps


def binary_search_last(arr, target):
    low = 0
    high = len(arr) - 1
    steps = 0
    result = -1

    while low <= high:
        steps += 1
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == target:
            result = mid
            low = mid + 1  # Продолжаем поиск вправо для последнего вхождения

        elif guess < target:
            low = mid + 1

        else:
            high = mid - 1

    return result, steps


def count_occurrences(arr, target):
    first_index, _ = binary_search_first(arr, target)  # Получаем индекс первого вхождения (игнорируем steps)
    last_index, _ = binary_search_last(arr, target)  # Получаем индекс последнего вхождения (игнорируем steps)

    if first_index == -1 or last_index == -1:
        return 0  # Элемент не найден

        # Количество = (последний индекс - первый индекс) + 1
    return last_index - first_index + 1


arr1 = [5, 10, 30, 35, 40, 45, 50, 50, 50, 50]
targets = range(51)

for target in targets:
    count = count_occurrences(arr1, target)
    print(f"Число {target} встречается {count} раз")
