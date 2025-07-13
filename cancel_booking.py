def user_cancel_booking():
    '''
        User provides 'email' and user is shown pnr's for their bookings.
        User is next asked to provide the pnr to delete the booking.
        If the provided pnr is not found, user is shown "No booking to cancel."
        Otherwise, 
            1. the booking is deleted from 'datastorage/bookings.txt'.
            2. The number of allocated_seats are increments by the number
               of seats in 'datastorage/bus_storage.txt'. 
            3. User is shown the message "Booking cancelled succesfully." 
    '''
    email= input("Enter your email: ")
    pnrs = []
    with open("datastorage/bookings.txt", "r") as bookings_file:
        for lines in bookings_file:
            line = lines.split(" ")
            if line[0].strip() == email:
                pnrs.append(line[1].strip())
    if (len(pnrs) == 0):
        print("No matching bookings found for the provided email.")
        return
    print("You have the following bookings, add pnr of the booking you want to cancel.")
    unique_pnrs = set(pnrs)
    print(*unique_pnrs)
    pnr_to_delete = input()
    num_seats = 0
    is_found = False
    busnumber = 0
    with open("datastorage/bookings.txt", "r") as bookings_file:
        for lines in bookings_file:
            line = lines.split(" ")
            if line[1].strip() == pnr_to_delete:
                num_seats += 1
                is_found = True
                busnumber = line[2].strip()
    if not is_found:
        print("No booking to cancel.")
        return
    with open("datastorage/bookings.txt", "r") as file:
        lines = file.readlines()
    with open("datastorage/bookings.txt", "w") as file:
        for line in lines:
            if line.split(" ")[1] != pnr_to_delete:
                file.write(line)
    with open("datastorage/bus_storage.txt", "r") as file:
        lines = file.readlines()
    with open("datastorage/bus_storage.txt", "w") as file:
        for line in lines:
            x = line.split(" ")
            if x[0] == busnumber:
                prev_booked_seats = int(x[7].strip())
                newline = "{} {} {} {} {} {} {} {}\n".format(
                    x[0], x[1], x[2], x[3], x[4], x[5], x[6], prev_booked_seats - num_seats)
                file.write(newline)
            else:
                file.write(line)
    print("Booking cancelled succesfully.")
                   