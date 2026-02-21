username = input("Enter your user name: ")

if len(username) > 12:
    print("username cannot exceed 12 characters.")
else:
    print(f"welcome {username}")