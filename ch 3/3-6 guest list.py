guests = ['stefan', 'emilia', 'sarah', 'peter', 'laura']

message1 = "you are welcome to dinner 2022-03-04"

for i in range(len(guests)):
    print(guests[i].title() +" "+ message1)

message2 = "cant make it to dinner"

print("\n" + guests[1].title() +" "+ message2 + "\n")

del guests[1]

guests.insert(1, 'johan')

for i in range(len(guests)):
    print(guests[i].title() +" "+ message1)

#print("i found a bigger table!")
message3 = "i found a bigger table!"
 #stuck here
print("\n" + ', '.join(guests).title() + f" {message3}\n")

guests.insert(0, 'karl')
    
half_list = len(guests)/2

guests.insert(int(half_list), 'linus')

guests.append('stefan')

for i in range(len(guests)):
    print(guests[i].title() +" "+ message1)

