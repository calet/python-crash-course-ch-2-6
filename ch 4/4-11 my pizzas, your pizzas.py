my_pizzas = ['hawaii', 'italian', 'mozzarella pesto']
friends_pizzas = my_pizzas[:]

my_pizzas.append('vegi')
friends_pizzas.append('kebab')

for Mpizza in my_pizzas:
    print(f"i like {Mpizza} pizzas")

print("\n")

for Fpizza in friends_pizzas:
    print(f"my friend like {Fpizza} pizzas")
    
print('\n')
print("we like these pizzas, but its unhealthy!")
