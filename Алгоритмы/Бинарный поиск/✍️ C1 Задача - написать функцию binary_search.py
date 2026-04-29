# ✍️Задача C1: Напишите функцию binary_search(arr, target)
"""""
 Функция должна:

Принимать отсортированный список arr и искомое значение target
Возвращать индекс элемента, если он найден
Возвращать -1, если элемент не найден
Использовать классический бинарный поиск с low, high, mid

"""""


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == target:
            return mid

        elif guess > target:
            high = mid - 1

        else:
            low = mid + 1

    return -1



# Тест: ищем число в списке:
arr1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
targets = [10, 5, 35, 0]  # ← список целей

for target in targets:
    index = binary_search(arr1, target)

    if index == -1:
        print(f"Число {target} не найдено в списке")

    else:
        print(f"Число {target} найдено на позиции {index}")
