import sys

# Function to create initial slam book
def initial_slambook():
    rows = int(input("How many friends do you want to add initially? "))
    slam_book = []

    for i in range(rows):
        print(f"\nEnter Friend {i+1} Details")
        print("-" * 40)

        name = input("Enter Name*: ")
        if name.strip() == "":
            sys.exit("Name is mandatory!")

        number = input("Enter Number*: ")
        if number.strip() == "":
            sys.exit("Number is mandatory!")

        about = input("Enter Something About Your Friend: ")
        dob = input("Enter Date of Birth (dd/mm/yyyy): ")
        category = input("Enter Category (Family/Friends/Work/Others): ")

        slam_book.append([name, number, about, dob, category])

    return slam_book


# Display all friends
def display_contacts(slam_book):
    if len(slam_book) == 0:
        print("\nNo records found!")
        return

    print("\n========== SLAM BOOK ==========")
    for i, friend in enumerate(slam_book, start=1):
        print(f"\nFriend {i}")
        print(f"Name     : {friend[0]}")
        print(f"Number   : {friend[1]}")
        print(f"About    : {friend[2]}")
        print(f"DOB      : {friend[3]}")
        print(f"Category : {friend[4]}")


# Add new friend
def add_contact(slam_book):
    print("\nAdd New Friend")

    name = input("Enter Name: ")
    number = input("Enter Number: ")
    about = input("Enter Something About Friend: ")
    dob = input("Enter DOB: ")
    category = input("Enter Category: ")

    slam_book.append([name, number, about, dob, category])
    print("Friend Added Successfully!")


# Search friend
def search_contact(slam_book):
    name = input("\nEnter name to search: ")

    found = False

    for friend in slam_book:
        if friend[0].lower() == name.lower():
            print("\nFriend Found")
            print("Name:", friend[0])
            print("Number:", friend[1])
            print("About:", friend[2])
            print("DOB:", friend[3])
            print("Category:", friend[4])
            found = True

    if not found:
        print("Friend not found.")


# Delete friend
def delete_contact(slam_book):
    name = input("\nEnter friend's name to delete: ")

    for friend in slam_book:
        if friend[0].lower() == name.lower():
            slam_book.remove(friend)
            print("Friend Deleted Successfully!")
            return

    print("Friend not found.")


# Menu
def menu():
    print("\n" + "=" * 40)
    print("      📖 SLAM BOOK MENU 📖")
    print("=" * 40)
    print("1. Display All Friends")
    print("2. Add New Friend")
    print("3. Search Friend")
    print("4. Delete Friend")
    print("5. Exit")
    print("=" * 40)


# Main Program
def main():
    slam_book = initial_slambook()

    while True:
        menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            display_contacts(slam_book)

        elif choice == "2":
            add_contact(slam_book)

        elif choice == "3":
            search_contact(slam_book)

        elif choice == "4":
            delete_contact(slam_book)

        elif choice == "5":
            print("\nThank you for using Slam Book!")
            break

        else:
            print("Invalid Choice! Try Again.")


if __name__ == "__main__":
    main()