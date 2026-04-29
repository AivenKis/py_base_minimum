def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        # Предполагаем, что текущий элемент — минимальный
        min_index = i

        # Ищем минимальный элемент в оставшейся части массива
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Меняем местами текущий элемент с найденным минимальным
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


arr = [64, 25, 12, 22, 11]
print("До:", arr)
selection_sort(arr)
print("После:", arr)
