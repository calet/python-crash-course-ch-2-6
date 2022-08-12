guests = ['stefan', 'emilia', 'sarah', 'peter', 'ture']

message1 = "you are welcome to dinner 2022-03-04"

for i in range(len(guests)):
    print(guests[i].title() +" "+ message1)

message2 = "cant make it to dinner"

print(guests[1] +" "+ message2)

del guests[1]

guests.insert(1, 'johan')

for i in range(len(guests)):
    print(guests[i].title() +" "+ message1)