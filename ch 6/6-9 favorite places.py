fav_places = {
    'johan': ['usa, ', 'mexico, ', 'turkey'],
    'emilia': ['sweden, ', 'spain, ', 'france, '],
    'peter': 'spain'
    }

for name, info in fav_places.items():
    print(f"name: {name}    countires: ", *info, )