numbered_list = []
ordinal_list = []
for i in range(1, 10):
    numbered_list.append(i)

intent = ('st', 'nd', 'rd', 'th')

for h in numbered_list:
    if str(h) == '1':
        ordinal_list.append(str(h) + intent[0])
    elif str(h) == '2':
        ordinal_list.append(str(h) + intent[1])
    elif str(h) == '3':
        ordinal_list.append(str(h) + intent[2])
    elif h != ',' and h != '[' and h != ']' and h != ' ' and h != '0':
        ordinal_list.append(str(h) + intent[3])
    
print('\n'.join(ordinal_list))