users = ['admin', 'johan', 'emilia', 'laura', 'kurt']

if users:
    for user in users:
        if user == 'admin':
            print("hello admin, would you like to see a status report?")
        else:
            print(f"hello {user}, thank you for logging in again!")
else:
    print("no users!")