events = {}

while True:
    print("\n--- EVENT TRACKER ---")
    print("1. Add Event")
    print("2. View Events")
    print("3. Exit")

    choice = input("Enter your choice: ")

    # Add Event
    if choice == "1":
        date = input("Enter date (DD-MM-YYYY): ")
        event = input("Enter event name: ")

        events[date] = event
        print("Event added successfully!")

    # View Events
    elif choice == "2":
        if len(events) == 0:
            print("No events found.")
        else:
            for date in events:
                print("Date:", date, "| Event:", events[date])

    # Exit
    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")