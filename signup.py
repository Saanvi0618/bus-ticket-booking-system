def user_signup():
    '''
        User provides 'name', 'email' and 'password'.
        The details will be stored in 'datastorage/user_storage.txt'.
    '''
    name = input("Enter name: ")
    email = input("Enter email: ")
    password = input("Enter password: ")

    user_data = f"\n{name} {email} {password}"

    with open("datastorage/user_storage.txt", "a") as user_storage_file:
        user_storage_file.write(user_data)

    print("Sign up successfull. Proceed to login")
