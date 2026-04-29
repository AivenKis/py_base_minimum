# Условие:
#  - написать функцию бинарного поиска: users_search (players, login) для поиска пользователя в системе по логину;
#  - если название логина пользователей совпадает (например: test1, test2) вернуть значение с количеством найденных совпадений

# Тестовые данные:
players = ["2fa_sms", "2test_amal", "alan1", "alan2", "alan3", "alan4", "bav0", "bav10", "bav9", "brv11", "brvpika1",
           "dove",
           "GTest", "ikis1", "ikis2", "ikis3", "ikis4", "juivplayer", "juivplayer_eu", "juivplayer0", "juivplayer1",
           "karPl_01",
           "karPl_02", "karPl_03", "karPl_04", "karPl_05", "karPl_06", "karPl_10", "karPl_11", "karPl_12", "karPl_13",
           "karPl_14",
           "Max", "me1", "me2", "me3", "me4", "Pasha", "Pasha1", "Pasha2", "pbtest", "pik1", "pika1", "pika10",
           "pika11", "pika12", "pika2", "pika3", "pika4", "pika5", "pika6", "pika7", "pika8", "pika9", "pikabet1502",
           "PikaKZT1",
           "PikaKZT2", "PikaKZT3",
           "player1", "player11", "player2", "player3", "player4", "proff", "proff1", "proff2", "proff3", "test1",
           "test1_amal",
           "test10_amal", "test123", "test2", "test2_amal", "test22_amal", "test2fa", "test3", "test3_amal",
           "test33_amal", "test4",
           "test4_amal", "test5_amal", "test6_amal", "testplayer1", "testplayer2", "testplayer3", "testplayer5", "uqp1",
           "uqp2", "vjik2", "vjik3", "yas1", "yas11", "yas2"]

logins = ['pika', 'ikis']


def find_first_prefix(arr, prefix):
    low = 0
    high = len(arr) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid].startswith(prefix):
            result = mid
            high = mid - 1

        elif arr[mid] < prefix:
            low = mid + 1

        else:
            high = mid - 1

    return result


def find_last_prefix(arr, prefix):
    low = 0
    high = len(arr) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid].startswith(prefix):
            result = mid
            low = mid + 1
        elif arr[mid] < prefix:
            low = mid + 1
        else:
            high = mid - 1
    return result


def users_search_with_logins(players, prefix):
    players_sorted = sorted(players)
    first = find_first_prefix(players_sorted, prefix)
    if first == -1:
        return 0, []  # количество 0, список пустой

    last = find_last_prefix(players_sorted, prefix)

    # Собираем все логины в диапазоне [first, last], которые начинаются с prefix
    found_logins = []
    for i in range(first, last + 1):
        if players_sorted[i].startswith(prefix):
            found_logins.append(players_sorted[i])

    count = len(found_logins)
    return count, found_logins


for login in logins:
    count, found_list = users_search_with_logins(players, login)
    if count > 0:
        logins_str = ", ".join(found_list)
        print(f"Логины, начинающиеся с '{login}': {count} шт. → {logins_str}")
    else:
        print(f"Пользователи с логином, начинающимся на '{login}', не найдены.")
