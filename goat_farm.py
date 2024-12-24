import datetime

# Initialize the records
goats = []

# Main menu function
def main_menu():
    while True:
        print("\nGoat Farm Management System")
        print("1. Record Goat Entry")
        print("2. Record Goat Exit")
        print("3. View All Records")
        print("4. Search Goat Records")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")
        if choice == "1":
            record_entry()
        elif choice == "2":
            record_exit()
        elif choice == "3":
            view_records()
        elif choice == "4":
            search_records()
        elif choice == "5":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Function to record goat entry
def record_entry():
    tag_id = input("Enter Goat Tag ID: ")
    age = input("Enter Goat Age: ")
    health_status = input("Enter Goat Health Status: ")
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    goat = {
        "Tag ID": tag_id,
        "Age": age,
        "Health Status": health_status,
        "Entry Date": date,
        "Exit Date": None,
        "Exit Reason": None
    }
    goats.append(goat)
    print("Goat entry recorded successfully!")

# Function to record goat exit
def record_exit():
    tag_id = input("Enter Goat Tag ID to mark as exited: ")
    for goat in goats:
        if goat["Tag ID"] == tag_id and goat["Exit Date"] is None:
            reason = input("Enter reason for exit: ")
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            goat["Exit Date"] = date
            goat["Exit Reason"] = reason
            print("Goat exit recorded successfully!")
            return
    print("Goat not found or already exited.")

# Function to view all records
def view_records():
    if not goats:
        print("No records available.")
    else:
        for goat in goats:
            print(goat)

# Function to search goat records
def search_records():
    tag_id = input("Enter Goat Tag ID to search: ")
    for goat in goats:
        if goat["Tag ID"] == tag_id:
            print(goat)
            return
    print("Goat not found.")

# Run the main menu
if __name__ == "__main__":
    main_menu()
