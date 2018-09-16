pizzas = ['pepperoni', 'sausage', 'canadian bacon', 'bbq chicken']
friend_pizzas = pizzas[:]

pizzas.append('bacon')
friend_pizzas.append('tuscan')

print("My favorite pizzas are: ")
for i in pizzas:
    print(i)

print("\nMy friend's favorite pizzas are:")
for i in friend_pizzas:
    print(i)