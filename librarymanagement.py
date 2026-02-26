library = {}

while True:
    print("\n------ LIBRARY MANAGEMENT SYSTEM ------")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. View Books")
    print("5. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        book_id = input("Enter Book ID: ")
        
        if book_id in library:
            print("Book already exists!")
        else:
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            
            library[book_id] = {
                "title": title,
                "author": author,
                "available": True
            }
            
            print("Book added successfully!")

    elif choice == 2:
        book_id = input("Enter Book ID to issue: ")
        
        if book_id not in library:
            print("Book not found!")
        elif library[book_id]["available"] == False:
            print("Book is already issued!")
        else:
            library[book_id]["available"] = False
            print("Book issued successfully!")
    elif choice == 3:
        book_id = input("Enter Book ID to return: ")
        
        if book_id not in library:
            print("Book not found!")
        elif library[book_id]["available"] == True:
            print("Book is already available in the library!")
        else:
            library[book_id]["available"] = True
            print("Book returned successfully!")
    elif choice == 4:
        print("\nAvailable Books in the Library:")
        for book_id, details in library.items():
            status = "Available" if details["available"] else "Issued"
            print(f"ID: {book_id}, Title: {details['title']}, Author: {details['author']}, Status: {status}")
    elif choice == 5:
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
        


