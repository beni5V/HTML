import sys


def initial_library():
    """Creates the initial library database."""
    return [
        ["The Hobbit", "J.R.R. Tolkien", 9780261102217, 1937, "Fantasy"]
    ]


def menu():
    """Displays the main menu."""
    print("\n" + "=" * 55)
    print("           SMART LIBRARY DIRECTORY")
    print("=" * 55)
    print("1. Add a New Book")
    print("2. View All Books")
    print("3. Exit")
    print("=" * 55)

    try:
        return int(input("Enter your choice (1-3): "))
    except ValueError:
        print("\n❌ Please enter a valid number!")
        return 0


def add_book(library):
    """Adds a new book to the library."""

    print("\n========== ADD NEW BOOK ==========")

    title = input("Book Title        : ")
    author = input("Author Name       : ")

    try:
        isbn = int(input("ISBN Number       : "))
    except ValueError:
        print("Invalid ISBN! Saved as 0.")
        isbn = 0

    try:
        year = int(input("Publication Year  : "))
    except ValueError:
        print("Invalid Year! Saved as 0.")
        year = 0

    genre = input("Genre             : ")

    library.append([title, author, isbn, year, genre])

    print("\n✅ Book added successfully!")


def display_books(library):
    """Displays all books in the library."""

    print("\n" + "=" * 85)
    print("{:<5} {:<25} {:<20} {:<15} {:<8} {:<12}".format(
        "No.", "Title", "Author", "ISBN", "Year", "Genre"))
    print("=" * 85)

    for i, book in enumerate(library, start=1):
        print("{:<5} {:<25} {:<20} {:<15} {:<8} {:<12}".format(
            i, book[0], book[1], book[2], book[3], book[4]))

    print("=" * 85)


def thanks():
    """Displays exit message."""

    print("\n" + "*" * 55)
    print("      Thank You for Using Our Library System!")
    print("             Have a Wonderful Day!")
    print("*" * 55)

    sys.exit()


library_db = initial_library()

print("=" * 55)
print("         WELCOME TO SMART LIBRARY DIRECTORY")
print("=" * 55)

while True:

    choice = menu()

    if choice == 1:
        add_book(library_db)

    elif choice == 2:
        display_books(library_db)

    elif choice == 3:
        thanks()

    else:
        print("\n❌ Invalid choice! Please select between 1 and 3.")