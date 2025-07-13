from signup import user_signup
from login import user_login
from booking import user_booking
from view_booking import user_view_booking
from cancel_booking import user_cancel_booking

def main():
    while (1):
        print("Press 1 to signup.")
        print("Press 2 to login.")
        print("Press 3 to book a ticket.")
        print("Press 4 to view bookings.")
        print("Press 5 to delete bookings.")
        print("Press any other key to exit.")
        user_option = int(input())

        match user_option:
            case 1:
                user_signup()
            case 2:
                user_login()
            case 3:
                user_booking()
            case 4:
                user_view_booking()
            case 5:
                user_cancel_booking()            
            case _:
                exit()    

if __name__ =="__main__":
    main()