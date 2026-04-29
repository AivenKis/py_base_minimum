def find_max_index(artists):
    """Находит индекс исполнителя с максимальным счётчиком"""
    max_index = 0
    max_plays = artists[0]["plays"]

    for i in range(1, len(artists)):
        if artists[i]["plays"] > max_plays:
            max_plays = artists[i]["plays"]
            max_index = i

    return max_index


def selection_sort_by_plays(artists):
    """Сортировка выбором по убыванию воспроизведений"""
    sorted_list = []

    # Копируем список, чтобы не изменять оригинал
    artists_copy = artists.copy()

    while artists_copy:
        # Находим исполнителя с максимальным счётчиком
        max_index = find_max_index(artists_copy)
        # Удаляем его из исходного и добавляем в отсортированный
        sorted_list.append(artists_copy.pop(max_index))

    return sorted_list


# Тестовые данные
my_music = [
    {"name": "Queen", "plays": 156},
    {"name": "Metallica", "plays": 423},
    {"name": "Pink Floyd", "plays": 89},
    {"name": "The Beatles", "plays": 512},
    {"name": "Nirvana", "plays": 1234},
    {"name": "Led Zeppelin", "plays": 178},
]

# Сортируем
sorted_music = selection_sort_by_plays(my_music)

# Выводим результат
print("🎵 Мои любимые исполнители:\n")
print(f"{'Место':<6} {'Исполнитель':<15} {'Прослушиваний'}")
print("-" * 40)

for i, artist in enumerate(sorted_music, 1):
    print(f"{i:<6} {artist['name']:<15} {artist['plays']}")
