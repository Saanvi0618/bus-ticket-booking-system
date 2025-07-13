def user_login():
    '''
        User provides 'email' and 'password' as the parameter.
        The provided 'email' and 'password' are matched against the entries
        in the file - 'datastorage/user_storage.txt'.
        If any entry matches, then user is shown a welcome message - "Welcome <name>"
        Otherwise, an error message is shown - "Provided email or password is incorrect."
    '''
    
    email = input("Enter email: ")
    password = input("Enter password: ")
    is_found = False
    name = ""
    with open("datastorage/user_storage.txt", "r") as user_storage_file:
        for t in user_storage_file:
            line = t.split(" ")
            if line[1].strip() == email and line[2].strip() == password:
                is_found = True
                name = line[0].strip()
                break
    if is_found:
        print("Welcome ", name)
    else:
        print("Provided email or password is incorrect.")
    