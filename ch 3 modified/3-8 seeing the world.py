#turn into dictonary
'''
locations = []
locations.append('usa - miami')
locations.append('spain - barcelona/madrid')
locations.append('egypt - pyramids')
locations.append('mexico - inca/mayan territory')
locations.append('mars/moon/ISS')
'''

locations = {
    'country': {
        'usa': {
            'point of intrest': 
                'miami',
        },
        'spain': {
            'point of intrest': 
                'barcelona/madrid',
        },
        'egypt': {
            'point of intrest': 
                'pyramids',
        },
        'mexico': {
            'point of intrest': 
                'mayan territory',
        }
    },
    'other': [
        'mars',
        'moon',
        'iss'
    ]
}

intrest_sorting_list = []
#print each key and value
for country in locations['country'].keys():
    for poi in locations['country'][country].values():
        #print(f"country: {country}\n-point of intrest: {poi}\n")
        intrest_sorting_list.append('\n-' + country +": "+ poi)
#print("other locations: ")
for oth in range(len(locations['other'])):
    #print(f"-{locations['other'][oth]}")
    intrest_sorting_list.append('\n-' + locations['other'][oth])

#sort keys and values

temp_sorted = sorted(intrest_sorting_list)
print("Temporary sorted locations order: " + ''.join(temp_sorted).title() + "\n")

print("Original locations order: " + ''.join(intrest_sorting_list).title() + "\n")

intrest_sorting_list.reverse()
print("Perm reverse location order: " + ''.join(intrest_sorting_list).title() + "\n")
intrest_sorting_list.reverse()
print("Perm reverse back to original location order: " + ''.join(intrest_sorting_list).title() + "\n")

intrest_sorting_list.sort()
print("Perm sorted locations order: " + ''.join(intrest_sorting_list).title() + "\n")

intrest_sorting_list.sort(reverse=True)
print("Perm reverse sorted location order: " + ''.join(intrest_sorting_list).title()  + "\n")
