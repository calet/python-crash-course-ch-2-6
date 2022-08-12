guests = ['stefan', 'emilia', 'sarah', 'peter', 'jack']

message1 = "you are welcome to dinner 2022-03-04"

for i in range(len(guests)):
    print(guests[i].title() +" "+ message1)

print(f"Guest amount: {len(guests)}")

message2 = "cant make it to dinner"

print("\n" + guests[1] +" "+ message2)

del guests[1]
print(f"Guest amount: {len(guests)}\n")
guests.insert(1, 'johan')
print(f"adding: {guests[1]}")

for i in range(len(guests)):
    print(guests[i].title() +" "+ message1)
print(f"Guest amount: {len(guests)}\n")