rivers = {
    'Germany': 'The Danube', 
    'china': 'The Yangtze', 
    'usa': 'the colorado'
    }

for country, river in rivers.items():
    print(f"{river.title()} flows through {country.title()}\n")

for country in rivers.keys():
    print(f"country: {country}")
print("\n")
for river in rivers.values():
    print(f"rivers: {river}")