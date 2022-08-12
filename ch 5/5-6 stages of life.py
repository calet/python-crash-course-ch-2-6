person_age = 22

if person_age < 2:
    stage = 'baby'
elif person_age < 4:
    stage = 'toddler'
elif person_age < 13:
    stage = 'kid'
elif person_age < 20:
    stage = 'teenager'
elif person_age < 65:
    stage = 'adult'
elif person_age > 65:
    stage = 'elder'

print(f"age: {person_age} stage in life: {stage}")