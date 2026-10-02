# PART 1 - BOOK LIST
books = [ "Harry Potter", "Matilda","The Jungle Book", "Charlotte's Web", "Wonder"]

print("==========================================")
print("       WELCOME TO THE SCHOOL LIBRARY")
print("==========================================")

print("Current Books:")
for book in books:
    print("-", book)


# PART 2 - LIST OPERATIONS
print("\nTotal Number of Books:", len(books))
print("First Book:", books[0])
print("Last Book:", books[-1])
print("First Three Books:", books[:3])


# PART 3 - ADDING AND REMOVING BOOKS
books.append("Diary of a Wimpy Kid")
print("\nAfter Adding a Book:")
print(books)

if "The Jungle Book" in books:
    books.remove("The Jungle Book")
    print("After Removing The Jungle Book:")
    print(books)


# PART 4 - SORTING BOOKS
books.sort()

print("\nBooks in Alphabetical Order:")
for book in books:
    print("-", book)


# PART 5 - LIBRARIAN DICTIONARY
librarian = {
    "name": "Ms. Aakifa",
    "section": "General Books",
    "experience": 5
}

print("\n==========================================")
print("           LIBRARIAN INFORMATION")
print("==========================================")

print("Name:", librarian["name"])
print("Section:", librarian["section"])
print("Experience:", librarian["experience"], "years")


# PART 6 - UPDATING DICTIONARY
librarian["experience"] = 6
librarian["email"] = "skzaakifastay@gmail.com"

print("\nUpdated Librarian Information:")
print(librarian)


# PART 7 - BOOK ID DIRECTORY
book_ids = [101, 102, 103, 104, 105]

book_names = [
    "Matilda",
    "Wonder",
    "Harry Potter",
    "Charlotte's Web",
    "Diary of a Wimpy Kid"
]

book_directory = dict(zip(book_ids, book_names))

print("\n==========================================")
print("             BOOK ID DIRECTORY")
print("==========================================")

for book_id, book_name in book_directory.items():
    print(book_id, ":", book_name)


# PART 8 - SEARCH FOR A BOOK
search_book = input("\nEnter a book name to search: ")

if search_book in books:
    print("Book Found:", search_book)
else:
    print("Sorry, the book is not available.")


# PART 9 - FINAL SUMMARY
print("\n==========================================")
print("          LIBRARY ORGANISER SUMMARY")
print("==========================================")

print("Total Available Books:", len(books))
print("Available Books:")

for book in books:
    print("-", book)

print("\nLibrarian:", librarian["name"])
print("Book Directory:", book_directory)

print("==========================================")
print("       THANK YOU FOR USING THE LIBRARY")
print("==========================================")

