guests = ['peter', 'laura', 'carl', 'sarah', 'rachel']

message1 = "you are welcome to dinner 2022-03-04"

for i in range(len(guests)):
    print(guests[i].title() +" "+ message1)

message2 = "cant make it to dinner"

print("\n" + guests[1].title() +" "+ message2 + "\n")

del guests[1]

guests.insert(4, 'johan')

for i in range(len(guests)):
    print(guests[i].title() +" "+ message1)

message3 = "i found a bigger table!"

print("\n" + ', '.join(guests).title() + f" {message3}\n")

guests.insert(0, 'karl')
    
half_list = len(guests)/2

guests.insert(int(half_list), 'linus')

guests.append('stefan')

for i in range(len(guests)):
    print(guests[i].title() +" "+ message1)

message4 = "sorry everyone, the new table will arrive late so i can only invite 2 of you"

#this part jumps over specific variables anywhere in list and pop the rest
m=0
while m != len(guests):
    if m != guests.index('johan') and m != guests.index('lisa'):
        popped = guests.pop(m)
        print("\n" + popped)
        guests.insert(m, popped)
        m = m+1
    else:
        m = m+1
        continue

print(guests)
print("\n")
for i in range(len(guests)):
    print(guests[i].title() +" "+ message1)

del guests[0]
del guests[0]

print(f"\nguests: {guests}")