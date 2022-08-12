animal1 = {'animal': 'cat', 'pet name': 'signe', 'owner': 'johan'}
animal2 = {'animal': 'dog', 'pet name': 'sture', 'owner': 'clara'}
animal3 = {'animal': 'cat', 'pet name': 'lira', 'owner': 'emilia'}

pets = [animal1, animal2, animal3]

for i in range(len(pets)):
    for k, v in pets[i].items():
        print(f"{k}", f"{v.title()}", sep=': ', end='    ')
    print('\n')