favorite_lang = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'johan': 'python',
    }

people = ['sarah', 'edward', 'stefan', 'emilia']

for poll in people:
    if poll in favorite_lang.keys():
        print(f"{poll} has already done the poll!")
    else:
        print(f"{poll} is allowed to participate in poll!")

new_dict = {}
for names, lang in favorite_lang.items():
    if lang not in new_dict:
        new_dict[lang] = names
    else:
        new_dict[lang] = new_dict[lang] + " and " + names

for lang, names in new_dict.items():
    print(f"\n{names} chose {lang}")

