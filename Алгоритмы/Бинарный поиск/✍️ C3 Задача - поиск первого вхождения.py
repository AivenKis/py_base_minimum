# ✍️ Задача C3: Измените функцию так, чтобы она возвращала индекс первого вхождения числа, если их несколько.

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
            high = mid - 1
        elif guess > target:
            high = mid - 1

        else:
            low = mid + 1

    return result, steps


arr1 = [5, 10, 30, 35, 40, 45, 50, 50, 50, 50]
targets = [3, 2, 50]

for target in targets:
    index, steps = binary_search_first(arr1, target)

    if index == -1:
        print(f"Число {target} не найдено в списке за {steps} шагов")

    else:
        print(f"Число {target} найдено на позиции {index} за {steps} шагов")
