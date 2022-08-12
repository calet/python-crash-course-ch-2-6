car = 'subaru'

#if car is a subaru
if car == 'subaru':
    print("is the car a subaru? true")
#if car has subaru
if 'subaru' in car:
    print(car == 'subaru')
#car is subaru and not audi
if 'subaru' in car and 'audi' not in car:
    print("is subaru in car and not audi? true")
#car is either subaru or audi
if 'subaru' in car or 'audi' in car:
    print("is car either subaru or audi? true")
#audi is not in car
if 'audi' not in car:
    print(car != 'audi')

#car is not an audi
print("\nis car an audi? false")
print(car == 'audi')

#is subaru an audi
print("is subaru an audi? false")
print('subaru' == 'audi')

#is length of subaru same as audi
print("is length of subaru equal to length of audi? false")
print(len('subaru') == len('audi'))

#is letter 3 in subaru and audi the same
car2 = 'audi'
print("is thee 3rd letter in subaru and audi the same? false")
print(car[3] == car2[3])

#is the length of subaru smaller or equal to length of audi
print("is the length of subaru smaller or equal to length of audi? false")
print(len(car) <= len(car2))