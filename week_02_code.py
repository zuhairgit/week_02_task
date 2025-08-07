#================= WEEK_02_TASKS ================

#----------------Task 1----------------
# students = ["Ali", "Fatima", "Zara", "Ahmed", "Usman"]
# for student in students:
#     print(student)

# # Reverse list without using reverse():

# reversed_students = students[::-1]
# print(reversed_students)


#---------------Task 2------------------

# Store 3 coordinates & unpack:
# coordinates = (10, 20, 30)
# x, y, z = coordinates
# print("x:", x, "y:", y, "z:", z)

# # Swap vars using tuple assignment:
# a = 5
# b = 10
# a, b = b, a
# print("a:", a, "b:", b)


#---------------Task 3-------------------

# Remove duplicates from list:
# nums = [1, 2, 2, 3, 4, 4, 5]
# unique_nums = list(set(nums))
# print(unique_nums)

# # Find intersection of two sets:
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# intersection = set1 & set2
# print(intersection)


#---------------Task 4---------------------

# # Student record CRUD in dict:
# students = {}

# # Create
# students["001"] = {"name": "Ali", "age": 20}
# # Read
# print(students["001"])
# # Update
# students["001"]["age"] = 21
# # Delete
# del students["001"]
# print(students)


# # Count word frequency in sentence:
# sentence = "the quick brown fox jumps over the lazy dog the fox was quick"
# words = sentence.split()
# freq = {}

# for word in words:
#     freq[word] = freq.get(word, 0) + 1

# print(freq)


#----------------Task 5------------------

# # Write calc(a, b, op):
# def calc(a, b, op):
#     if op == '+':
#         return a + b
#     elif op == '-':
#         return a - b
#     elif op == '*':
#         return a * b
#     elif op == '/':
#         return a / b if b != 0 else "Error: Divide by zero"
#     else:
#         return "Invalid operator"

# print(calc(10, 5, '+'))

# # Write factorial(n) recursive:
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)

# print(factorial(5))

#-----------------Task 6---------------

# import random
# from datetime import datetime

# print("Random number:", random.randint(1, 100))
# print("Current datetime:", datetime.now())

# def add(a, b):
#     return a + b

# def square(n):
#     return n * n

# import math_utils

# print(math_utils.add(2, 3))
# print(math_utils.square(4))

#-----------------Task 7---------------


# 35Safe int input loop:
# Keeps asking until the user provides a valid integer.

# while True:
#     user_input = input("Enter an integer: ")
#     try:
#         number = int(user_input)
#         print("You entered:", number)
#         break
#     except ValueError:
#         print("Invalid input. Please enter a valid integer.")

# # File open with error message:
# # Attempts to open a file and handles the error if the file is missing.
# filename = "data.txt"

# try:
#     with open(filename, 'r') as file:
#         content = file.read()
#         print("File content:\n", content)
# except FileNotFoundError:
#     print(f"Error: The file '{filename}' does not exist.")


#----------------Task 8-----------------


import json

FILENAME = "phonebook.json"

# Load contacts from file
def load_phonebook():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except:
        return {}  # Return empty phonebook if file doesn't exist or is empty

# Save contacts to file
def save_phonebook(phonebook):
    with open(FILENAME, "w") as file:
        json.dump(phonebook, file, indent=4)

# Add a contact
def add_contact(phonebook):
    name = input("Enter name: ")
    number = input("Enter phone number: ")
    phonebook[name] = number
    print("Contact added.")

# View all contacts
def view_contacts(phonebook):
    if not phonebook:
        print("No contacts found.")
    else:
        for name, number in phonebook.items():
            print(f"{name}: {number}")

# Update a contact
def update_contact(phonebook):
    name = input("Enter name to update: ")
    if name in phonebook:
        number = input("Enter new phone number: ")
        phonebook[name] = number
        print("Contact updated.")
    else:
        print("Contact not found.")

# Delete a contact
def delete_contact(phonebook):
    name = input("Enter name to delete: ")
    if name in phonebook:
        del phonebook[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")

# Main menu
def main():
    phonebook = load_phonebook()

    while True:
        print("\nPhonebook Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_contact(phonebook)
        elif choice == "2":
            view_contacts(phonebook)
        elif choice == "3":
            update_contact(phonebook)
        elif choice == "4":
            delete_contact(phonebook)
        elif choice == "5":
            save_phonebook(phonebook)
            print("Phonebook saved. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Run the app
if __name__ == "__main__":
    main()




