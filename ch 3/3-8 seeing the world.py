locations = []
locations.append('usa - miami')
locations.append('spain - barcelona/madrid')
locations.append('egypt - pyramids')
locations.append('mexico - inca/mayan territory')
locations.append('mars/moon/ISS')

temp_sorted = sorted(locations)
print("Temporary sorted locations order: " + ', '.join(temp_sorted).title() + "\n")

print("Original locations order: " + ', '.join(locations).title() + "\n")

locations.reverse()
print("Perm reverse location order: " + ', '.join(locations).title() + "\n")
locations.reverse()
print("Perm reverse back to original location order: " + ', '.join(locations).title() + "\n")

locations.sort()
print("Perm sorted locations order: " + ', '.join(locations).title() + "\n")

locations.sort(reverse=True)
print("Perm reverse sorted location order: " + ', '.join(locations).title() + "\n")