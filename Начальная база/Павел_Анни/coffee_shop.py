# Сначала мы создали списки
drinks = ["hot chocolate", "coffee", "milkshake", "black tea"]
flavors = ["caramel", "vanilla", "peppermint", "raspberry", "banana", "plain"]
toppings = ["chocolate", "cinnamon", "caramel", "condensed milk"]

print("Erik's Coffee Shop drinks")
print("-------------------------")

# Затем мы вывели списки с помощью циклов. А затем мы вывели цифры рядом с каждым напитком или вкусом

i = int(1)
for d in drinks:
    print(i, d)
    i = i + 1
drink = input("Choose your drink")

print("Erik's Coffee Shop flavors")
print("-------------------------")

i = int(1)
for f in flavors:
    print(i, f)
    i = i + 1
flavor = input("Choose your flavor")

print("Erik's Coffee Shop flavors")
print("-------------------------")

i = int(1)
for t in toppings:
    print(i, t)
    i = i + 1
topping = input("Choose your topping: ")

print("Here is your order: ")
print("Main product: ", drinks[int(drink) - 1])
print("Flavor: ", flavors[int(flavor) - 1])
print("Topping: ", toppings[int(topping) - 1])
print("Thanks for your order!")
