# 							Есть два словаря: рецепт пирога и запасы.
# Написать функцию, которая будет определять, сколько можно испечь пирогов из имеющихся запасов

recipe = {'bread': 200, 'sugar': 10, 'salt': 100, 'milk': 50, 'eggs': 2}
storage = {'bread': 200, 'sugar': 10, 'salt': 100, 'milk': 50,  'eggs': 2}


def max_pies(recipe, storage):
	possible_pies = float('inf')  # Начинаем с большого числа
	
	for ingredient, amount in recipe.items():
		if ingredient not in storage or storage[ingredient] < amount:
			return 0  # Если ингредиента нет или его недостаточно, то готовить нельзя
		
		possible_pies = min(possible_pies, storage[ingredient] // amount)
	
	return possible_pies


print(max_pies(recipe, storage))

# 						Логика решения:
# 	 Для каждого ингредиента из recipe проверяем, сколько у нас есть в storage.
#    Вычисляем, на сколько пирогов хватит каждого ингредиента:
#    количество пирогов = количество ингредиента в storage необходимое количество в recipe
#    количество пирогов = необходимое количество в recipe количество ингредиента в storage​
#    Минимальное значение из этих расчетов — это количество пирогов, которое можно испечь.
