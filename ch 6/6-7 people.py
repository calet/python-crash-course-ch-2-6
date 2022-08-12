person1 = {'name': 'johan', 'age': '22', 'favorite dessert': 'cake'}
person2 = {'name': 'emilia', 'age': '20', 'favorite dessert': 'pancakes'}
person3 = {'name': 'carl', 'age': '25', 'favorite dessert': 'cookies'}

person_list = [person1, person2, person3]
for amount in range(len(person_list)):
    for k, v in person_list[amount].items():
            print(f"{k}", f"{v.title()}", sep=":", end="    ")
    print("\n")