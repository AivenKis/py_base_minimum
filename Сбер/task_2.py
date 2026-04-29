# Написать функцию, которая выводит все элементы массива, имеющие заданную строку.

# Ответ для подстроки sber в list_sample будет:  'sbermarket','sberID', 'sberWeather', 'megasbermarket', 'sberTaxi'

list_sample = ['adkn', 'jjjfje', '12ufbbb','aaai', 'sbermarket','sberID', 'sberWeather', 'megasbermarket', 'sberTaxi']


def find_elements_with_substring(array, substring):
	"""
	Функция находит все элементы массива, содержащие заданную подстроку

	Args:
		array (list): Исходный массив строк
		substring (str): Искомая подстрока

	Returns:
		list: Список элементов, содержащих подстроку
	"""
	result = []
	for element in array:
		if substring in element:
			result.append(element)
	return result


# Пример использования
list_sample = ['adkn', 'jjjfje', '12ufbbb', 'aaai', 'sbermarket', 'sberID', 'sberWeather', 'megasbermarket', 'sberTaxi']
substring = 'sber'

matching_elements = find_elements_with_substring(list_sample, substring)
print(f"Ответ для подстроки {substring} в list_sample будет: {', '.join(repr(item) for item in matching_elements)}")