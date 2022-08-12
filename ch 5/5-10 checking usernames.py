current_users = ['admin', 'stefan', 'emilia', 'sarah', 'peter']


new_users = ['Admin', 'johan', 'Carl', 'erik', 'jonas']

case_insensitive_users = []

for user in current_users:
    case_insensitive_users.append(user.lower())
for new_user in new_users:
    if new_user.lower() in case_insensitive_users:
        print(f"{new_user}, this user already exist!")
    else:
        print(f"{new_user}, this username is available!")