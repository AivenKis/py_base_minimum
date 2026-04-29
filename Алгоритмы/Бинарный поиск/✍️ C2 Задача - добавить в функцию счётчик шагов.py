# ✍️ Задача C2 (дополнительно): Добавьте счётчик шагов,
# Модифицируйте функцию так, чтобы она возвращала не только индекс, но и количество шагов (итераций цикла).
# 💡 Подсказка: заведите переменную steps = 0 и увеличивайте её на каждой итерации.


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    steps = 0

    while low <= high:
        steps += 1
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == target:
            return mid, steps

        elif guess > target:
            high = mid - 1

        else:
            low = mid + 1

    return -1, steps


# Тест: ищем число в списке:
arr1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
targets = [10, 5, 35, 0]  # ← список целей

for target in targets:
    index, steps = binary_search(arr1, target)

    if index == -1:
        print(f"Число {target} не найдено в списке за {steps} шагов")

    else:
        print(f"Число {target} найдено на позиции {index} за {steps} шагов")
