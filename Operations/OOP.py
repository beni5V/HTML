import os

FILE_NAME = "records.txt"

def initialize_database():
    """Creates the text file database if it doesn't already exist."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as file:
            pass

def add_record():
    """Appends a new line entry to the data file."""
    print("\n--- Add Entry ---")
    record_id = input("Enter ID: ").strip()
    name = input("Enter Name: ").strip()
    score = input("Enter Score: ").strip()

    if not record_id or not name or not score:
        print("Error: Fields cannot be empty.")
        return

    with open(FILE_NAME, "a") as file:
        file.write(f"{record_id}|{name}|{score}\n")
    print("Record saved.")

def view_all_records():
    """Uses the .read() function to process and display all data."""
    print("\n--- All Database Records ---")
    initialize_database()

    with open(FILE_NAME, "r") as file:
        full_content = file.read()

    if not full_content.strip():
        print("The database file is currently empty.")
        return
    lines = full_content.strip().split("\n")

    print(f"{'ID':<10}{'Name':<20}{'Score':<10}")
    print("-" * 40)
    
    for line in lines:
        if line.strip():
            rec_id, name, score = line.split("|")
            print(f"{rec_id:<10}{name:<20}{score:<10}")

def search_record():
    """Uses .read() to pull entire text data and search for an identity match."""
    print("\n--- Search Record ---")
    search_id = input("Enter ID to search for: ").strip()

    with open(FILE_NAME, "r") as file:
        full_content = file.read()

    if not full_content.strip():
        print("No records to search.")
        return

    lines = full_content.strip().split("\n")
    found = False

    for line in lines:
        if line.strip():
            rec_id, name, score = line.split("|")
            if rec_id == search_id:
                print(f"\nMatch Found!\nID: {rec_id}\nName: {name}\nScore: {score}")
                found = True
                break
                
    if not found:
        print("Record ID not found.")

def main():
    initialize_database()
    while True:
        print("\n==============================")
        print("   PYTHON .READ() PROJECT     ")
        print("==============================")
        print("1. Add Record (Append)")
        print("2. View All Records (Using read())")
        print("3. Search Records (Using read())")
        print("4. Exit")
        
        choice = input("\nSelect menu option (1-4): ").strip()
        
        if choice == "1":
            add_record()
        elif choice == "2":
            view_all_records()
        elif choice == "3":
            search_record()
        elif choice == "4":
            print("\nExiting program.")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
