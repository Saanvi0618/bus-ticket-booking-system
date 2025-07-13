import random
def user_booking():
    '''
        User provides 'email', 'from_station', 'to_station' and 'num_passengers' as the parameter.
        If no bus is available, user is shown "No matching bus found".
        Otherwise,
            1. User is shown the details of the matching buses.
            2. User provides the 'bus_number' for which they need to book the ticket.
            3. Accordingly, booked_seats are incremented in 'datastorage/bus_storage.txt'.
            4. User provides the passenger names and their age which are added in 'datastorage/bookings.txt'.
            5. At the end, user is shown the message "Booking is complete".
    '''
    email = input("enter email: ")
    from_station = input("enter station: ")
    to_station = input("enter destination: ")
    num_passengers = int(input("enter number of passengers: "))
    is_found = False
    matching_buses = []
    with open("datastorage/bus_storage.txt", "r") as bookings_file:
        for lines in bookings_file:
            line = lines.split(" ")
            try:
                total_seats = int(line[6].strip())
                booked_seats = int(line[7].strip())
                available_seats = total_seats - booked_seats
            except:
                pass
            if line[2].strip() == from_station and line[3].strip() == to_station and num_passengers <= available_seats:
                is_found = True
                matching_buses.append((line[0].strip(), line[1].strip(), line[4].strip(), line[5].strip()))
    if is_found:
        print("\nBusNumber BusName DepartureTime ArrivalTime")
        for matching_bus in matching_buses:
            print(*matching_bus)       
    else:
        print("No matching bus found.")
    user_provided_bus_number = input("Enter bus number to book a ticket: ")
    with open("datastorage/bus_storage.txt", "r") as file:
        lines = file.readlines()
    with open("datastorage/bus_storage.txt", "w") as file:
            for line in lines:
                x = line.split(" ") 
                if x[0] == user_provided_bus_number:
                    booked_seats = int(x[7].strip())
                    new_line = "{} {} {} {} {} {} {} {}\n".format(
                        x[0], x[1], x[2], x[3], x[4], x[5], x[6], booked_seats + num_passengers)
                    file.write(new_line)
                else:
                    file.write(line)
    # Find the bus number in bus_storage.txt and increase the booked seats by
    # num_passenger
    
    with open("datastorage/bookings.txt", "a") as file:
        for _ in range(num_passengers):
            passenger_name = input("Enter passenger name: ")
            passenger_age = input("Enter passenger age: ")
            pnr = random.randint(1, 20000000)
            print(pnr)
            user_data = f"\n{email} {pnr} {user_provided_bus_number} {from_station} {to_station} {passenger_name} {passenger_age}"
            file.write(user_data)

    print("Booking is complete.")
