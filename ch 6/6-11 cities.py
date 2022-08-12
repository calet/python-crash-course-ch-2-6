cities = {
    'göteborg': {
        'country': 'usa', 'population': '1 060 000', 'fact': 'one of swedens biggest cities'
        },
    'kiruna': {
        'country': 'sweden', 'population': '17 513', 'fact': 'location of esrange'
        },
    'stockholm': {
        'country': 'stockholm', 'population': '975 551', 'fact': 'capital of sweden'
        }
    }

for city, information in cities.items():
    for info, values in information.items():
        print(f"{city}: {info}: {values}")
    print('\n')