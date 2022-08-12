
cars = []
cars.append('ferrari')
cars.append('rolls royce')
print("cars: " + ', '.join(cars).title())
print(f"amount of cars: {len(cars)}" + '\n')

cars.insert(1, 'bmw')
cars.insert(0, 'tesla')
print("cars: " + ', '.join(cars).title())
print(f"amount of cars: {len(cars)}" + '\n')

#add into a dictonary

cars.sort()
print("perm sorted: " + ', '.join(cars).title() + "\n")
cars.reverse()
print("reversed: " + ', '.join(cars).title() + "\n")
temp_sort = sorted(cars)
print("temp sorted: " + ', '.join(temp_sort).title() + "\n")

#sort dictonary

for i in range(len(cars)):
    popped = cars.pop(i)
    cars.insert(i, popped)
    position = cars.index(popped)
    print(f"car: {popped} is on position {position}")
    
removed = 'bmw'
cars.remove(removed)
print('\n')
print(f"removing: {removed.upper()}" + "\n")

print("cars: " + ', '.join(cars).title())
print(f"amount of cars: {len(cars)}" + '\n')

#pop and remove cars from the dictonary

m = 0
while m != len(cars):
    if m != cars.index('rolls royce'):
        print(f"deleting: {cars[m].lower()}")
        del cars[m]
    else:
        m = m+1
        continue

#what car got deleted

print("\n")
print("cars: " + ', '.join(cars).title())
print(f"amount of cars: {len(cars)}" + '\n')

#how many cars are there in dictonary