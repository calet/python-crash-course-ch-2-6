cubes = []

for c in range(1, 11):
    cubes.append(c**3)

middle = cubes[int(len(cubes)/3)+1:int(len(cubes)-4)]

print(f"whole list: {', '.join(map(str, cubes))}\n")
print(f"the first three items in the list are: {', '.join(map(str, cubes[:3]))}\n")
print(f"two items from the middle of the list are: {', '.join(map(str, middle))}\n")
print(f"the last 3 items in the list are: {', '.join(map(str, cubes[7:]))}")

