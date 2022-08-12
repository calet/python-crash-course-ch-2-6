peoples_fav_number = {
    'emilia': {'number': '5', 'age': '20'},
    'rizwan': {'number': '29', 'age': '22'},
    'emil': {'number': '50', 'age': '24'},
    'emma': {'number': '30', 'age': '19'}
    }

for person, number in peoples_fav_number.items():
    print(f"{person}: {number['number']}")