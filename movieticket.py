class MovieBooking:

    movies = ["Movie1 - 10AM",
              "Movie2 - 2PM",
              "Movie3 - 6PM"]

    seats = ["A1", "A2", "A3", "A4", "A5"]
    booked = []

    while True:
        print("\n1. Book Ticket")
        print("2. Exit")
        choice = input("Enter choice: ")

        if choice == "1":

            print("\nAvailable Movies:")
            for i in range(len(movies)):
                print(i + 1, ".", movies[i])

            movie_choice = int(input("Select movie number: "))

            if 1 <= movie_choice <= len(movies):

                print("\nAvailable Seats:")
                for seat in seats:
                    if seat not in booked:
                        print(seat, end=" ")
                print()

                seat_choice = input("Enter seat number: ")

                if seat_choice in seats and seat_choice not in booked:
                    booked.append(seat_choice)

                    print("\n---- Booking Confirmation ----")
                    print("Movie:", movies[movie_choice - 1])
                    print("Seat:", seat_choice)
                    print("Booking Successful ✅")
                else:
                    print("Seat Not Available!")

            else:
                print("Invalid Movie Number!")

        elif choice == "2":
            print("Thank You!")
            break

        else:
            print("Wrong Choice!")


# Create Object
system = MovieBooking()