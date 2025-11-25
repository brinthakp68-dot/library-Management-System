import os

BOOK_FILE = "books.txt"
ISSUE_FILE = "issued.txt"

def add_book():
    book_id = input("Enter Book ID: ")
    book_name = input("Enter Book Name: ")

    with open(BOOK_FILE, "a") as f:
        f.write(f"{book_id},{book_name}\n")

    print("✅ Book Added Successfully")


def display_books():
    if not os.path.exists(BOOK_FILE):
        print("No books available")
        return

    print("\nAVAILABLE BOOKS")
    print("ID\tNAME")
    print("----------------")
    with open(BOOK_FILE, "r") as f:
        for line in f:
            book_id, book_name = line.strip().split(",")
            print(f"{book_id}\t{book_name}")


def issue_book():
    student_name = input("Enter Student Name: ")
    book_id = input("Enter Book ID to Issue: ")

    books = open(BOOK_FILE, "r").readlines()
    issued = open(ISSUE_FILE, "a")

    for line in books:
        if line.startswith(book_id + ","):
            issued.write(f"{student_name},{line}")
            print("✅ Book Issued Successfully")
            return

    print("❌ Book not available")


def return_book():
    book_id = input("Enter Book ID to Return: ")

    if not os.path.exists(ISSUE_FILE):
        print("No issued books")
        return

    lines = open(ISSUE_FILE, "r").readlines()

    with open(ISSUE_FILE, "w") as f:
        for line in lines:
            if not line.split(",")[1] == book_id:
                f.write(line)

    print("✅ Book Returned Successfully")


def view_issued_books():
    if not os.path.exists(ISSUE_FILE):
        print("No issued books")
        return

    print("\nISSUED BOOKS")
    print("Student\tBook ID\tBook Name")
    print("--------------------------------")
    with open(ISSUE_FILE, "r") as f:
        for line in f:
            student, book_id, book_name = line.strip().split(",")
            print(f"{student}\t{book_id}\t{book_name}")


def menu():
    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. View Issued Books")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            display_books()
        elif choice == "3":
            issue_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            view_issued_books()
        elif choice == "6":
            print("Thank you 😊")
            break
        else:
            print("Invalid choice")


menu()
