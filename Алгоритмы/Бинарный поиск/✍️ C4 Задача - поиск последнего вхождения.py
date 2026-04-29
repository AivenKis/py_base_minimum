# ✍️ Задача C4: Напишите функцию binary_search_last(arr, target), которая возвращает индекс последнего вхождения числа.

def binary_search_last(arr, target):
    low = 0
    high = len(arr) - 1
    steps = 0
    result = -1

    while low <= high:
        steps += 1
        mid = (low + high) // 2  # Вычисляется индекс середины текущего диапазона
        guess = arr[mid]  # Получаем значение элемента массива по индексу mid и сохраняем в переменную guess

        if guess == target:
            result = mid
            low = mid + 1

        elif guess < target:
            low = mid + 1

        else:
            high = mid - 1

    return result, steps


arr1 = [1, 2.5, 5, 10, 30, 35, 40, 45, 50, 50]
targets = [3, 1, 50]

for target in targets:
    index, steps = binary_search_last(arr1, target)

    if index == -1:
        print(f"Число {target} не найдено в списке за {steps} шагов")

    else:
        print(f"Число {target} найдено на позиции {index} за {steps} шагов")
