def user_view_booking():
    '''
    User provides an email for which they want to view the bookigs.
    If no bookings exist for the email, user is shown "No bookings available for the provided email id".
    Otherwise,
        1. User is shown the pnrs.
        2. User selects a pnr
        3. All the details for the pnr are shown to the user.
    '''
    email= input("Enter your email: ")
    pnrs = []
    with open("datastorage/bookings.txt", "r") as bookings_file:
        for z in bookings_file:
            line = z.split(" ")
            if line[0].strip() == email:
                pnrs.append(line[1].strip())
    if (len(pnrs) == 0):
        print ("No bookings available for the provided email id.")
    else:
        print("You have the following bookings, type the pnr you want to view.")
        print(*pnrs)
        pnr = input()
        if pnr not in pnrs:
            print("Select a valid pnr.")
        else:
            with open("datastorage/bookings.txt", "r") as bookings_file:
                for z in bookings_file:
                    line = z.split(" ")
                    if line[0].strip() == email and line[1].strip() == pnr:
                        print("Email:",line[0], "pnr:",line[1], "bus_no:",line[2], "from:",line[3], "to:",line[4], "passenger_name:",line[5], "passenger_age:",line[6])
                        print("pnr:",line[1])
                        print("bus_no:",line[2])
                        print("from:",line[3])
                        print("to:",line[4])
                        print("passenger_name:",line[5])
                        print("passenger_age:",line[6])
                        break 
        
