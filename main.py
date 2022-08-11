seat_availablity1 = 3
seat_availablity2 = 2
seat_availablity3 = 5
no_of_seat_filled = 0

total_seats_available = seat_availablity1 + seat_availablity2 + seat_availablity3
print("WELCOME")
while total_seats_available > no_of_seat_filled:
    print("Total number of seats available= " + str(total_seats_available))
    coach_name = input("Enter the coach in which you want to get reserved:-\n(a) Sleeper\n(b) AC\n(c) General\n")
    if coach_name == "Sleeper":

        while seat_availablity1 > no_of_seat_filled:
            print("Number of seats available= " + str(seat_availablity1) + "\nEnter BOOK if you want to book")
            booking_status = input("\n")
            if booking_status == "BOOK":
                print("\nBOOKED")
            elif booking_status == "book":
                print("Wirte in capital letters!")
            elif booking_status == "Book":
                print("Write all letters in capital!")
            else:
                print("\nNOT BOOKED")
            if booking_status == "BOOK":
                seat_availablity1 -= 1

        print("Seat is Unavailable")
    if coach_name == "sleeper":
        print("Enter sleeper as 'Sleeper'")

    if coach_name == "AC":

        while seat_availablity2 > no_of_seat_filled:
            print("Number of seats available= " + str(seat_availablity2) + "\nEnter BOOK if you want to book")
            booking_status = input("\n")
            if booking_status == "BOOK":
                print("\nBOOKED")
            elif booking_status == "book":
                print("Wirte in capital letters!")
            elif booking_status == "Book":
                print("Write all letters in capital!")
            else:
                print("\nNOT BOOKED")
            if booking_status == "BOOK":
                seat_availablity2 -= 1

        print("Seat is Unavailable")
    if coach_name == "ac":
        print("Enter ac as 'AC'")

    if coach_name == "General":

        while seat_availablity > no_of_seat_filled:
            print("Number of seats available= " + str(seat_availablity3) + "\nEnter BOOK if you want to book")
            booking_status = input("\n")
            if booking_status == "BOOK":
                print("\nBOOKED")
            elif booking_status == "book":
                print("Wirte in capital letters!")
            elif booking_status == "Book":
                print("Write all letters in capital!")
            else:
                print("\nNOT BOOKED")
            if booking_status == "BOOK":
                seat_availablity3 -= 1

        print("Seat is Unavailable")
    if coach_name == "general":
        print("Enter general as 'General'")

    total_seats_available = seat_availablity1 + seat_availablity2 + seat_availablity3
print("The seats are unavailable in this train!")