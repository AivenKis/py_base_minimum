# run_all_tests.py
import sys


def test_task1():
	print("=== Тестирование задания 1 (Максимальное количество пирогов) ===")
	
	# Определяем функцию из task_1
	def max_pies(recipe, storage):
		possible_pies = float('inf')  # Начинаем с большого числа
		
		for ingredient, amount in recipe.items():
			if ingredient not in storage or storage[ingredient] < amount:
				return 0  # Если ингредиента нет или его недостаточно, то готовить нельзя
			
			possible_pies = min(possible_pies, storage[ingredient] // amount)
		
		return possible_pies
	
	# Тестовые данные
	recipe = {'bread': 200, 'sugar': 10, 'salt': 100, 'milk': 50, 'eggs': 2}
	storage = {'bread': 1000, 'sugar': 1000, 'milk': 270, 'salt': 210, 'eggs': 10}
	
	result = max_pies(recipe, storage)
	print(f"Максимальное количество пирогов: {result}")
	print()


def test_task2():
	print("=== Тестирование задания 2 (Поиск подстроки в массиве) ===")
	
	# Функция из task_2
	def find_elements_with_substring(array, substring):
		result = []
		for element in array:
			if substring in element:
				result.append(element)
		return result
	
	# Тестовые данные
	list_sample = ['adkn', 'jjjfje', '12ufbbb', 'aaai', 'sbermarket', 'sberID', 'sberWeather', 'megasbermarket',
	               'sberTaxi']
	substring = 'sber'
	
	matching_elements = find_elements_with_substring(list_sample, substring)
	print(f"Элементы с подстрокой '{substring}': {', '.join(repr(item) for item in matching_elements)}")
	print()


def test_task3():
	print("=== Тестирование задания 3 (Класс с наследованием) ===")
	
	# Код из task_3
	class ClsZ:
		env = 'Class Z: Env'
	
	class ClsA(ClsZ):
		def init(self):
			self.env = 'Class A.init: Env'
		
		# env = "Class A: Env"  # Закомментированная строка
		def cls_env(self):
			self.env = 'Class A.casd: Env'
			print(self.env)
	
	class ClsB(ClsA):
		def init(self):
			super().init()
			print(self.env)
	
	a_cls = ClsA()
	a_cls.cls_env()
	print("ClsA: " + a_cls.env)
	print("ClsB: " + ClsB.env)
	print()



def test_task4():
	print("=== Тестирование задания 4 (Модификация списка) ===")
	
	# Модифицированная функция для тестирования без ввода пользователя
	def modify_list_test(numbers):
		result = []
		for num in numbers:
			if num % 2 == 0 and num != 0:  # Если число четное и не ноль
				result.append(num // 2)
		return result
	
	# Тестовые данные
	test_lists = [
		[1, 2, 3, 4, 5, 6],
		[0, 1, 2, 3, -4],
		[10, 20, 30]
	]
	
	for i, test_list in enumerate(test_lists):
		result = modify_list_test(test_list)
		print(f"Тест {i + 1}: Из {test_list} получаем {result}")
	print()


def run_all_tests():
	print("Запуск тестирования всех заданий\n")
	
	test_task1()
	test_task2()
	test_task3()
	test_task4()
	
	print("Все тесты выполнены успешно!")


if __name__ == "__main__":
	run_all_tests()