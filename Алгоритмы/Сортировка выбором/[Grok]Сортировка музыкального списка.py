"""
Топ любимых исполнителей по количеству прослушиваний
Сортировка по убыванию воспроизведений
"""

# Ваша музыкальная библиотека
music = [
    {"artist": "The Beatles", "plays": 842},
    {"artist": "Metallica", "plays": 1567},
    {"artist": "Daft Punk", "plays": 723},
    {"artist": "Queen", "plays": 1615},
    {"artist": "Arctic Monkeys", "plays": 489},
    {"artist": "Linkin Park", "plays": 912},
    {"artist": "Nirvana", "plays": 2378},
    {"artist": "Radiohead", "plays": 654},
    {"artist": "Imagine Dragons", "plays": 298},
    {"artist": "Pink Floyd", "plays": 981},
]

# Сортировка по убыванию количества прослушиваний
sorted_music = sorted(music, key=lambda x: x["plays"], reverse=True)

# Красивый вывод топа
print("🎵 Ваш музыкальный ТОП 🎵\n")
print(f"{'№':<3} {'Исполнитель':<25} {'Прослушиваний':<12}")
print("—" * 50)

for place, entry in enumerate(sorted_music, 1):
    artist = entry["artist"]
    plays = entry["plays"]

    # Подсвечиваем топ-3
    if place == 1:
        medal = "🥇"
    elif place == 2:
        medal = "🥈"
    elif place == 3:
        medal = "🥉"
    else:
        medal = "  "

    print(f"{medal} {place:<2} {artist:<25} {plays:,} раза")
