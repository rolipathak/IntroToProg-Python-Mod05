# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RPathak,2/26/2025,Created Script
#  ------------------------------------------------------------------------------------------ #
import json
# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
#FILE_NAME: str = "Enrollments.csv"
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data in a dictionary (TODO: Change this to a Dictionary)
students: list = []  # a table of student data
json_data: str = ''  # Holds students data in json file format.
csv_data: str = ''  # Holds combined CSV data. Note: Remove later since it is NOT needed with the JSON File
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.


# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
try:
    file = open(FILE_NAME, "r") # open json file in read mode
    students = json.load(file) # When the program starts, the contents of the "Enrollments.json" are automatically read into a two-dimensional list table (a list of dictionary rows).
    file.close() #close file
except Exception as e: # exception handling; store error message in variable e if the above code throws error
    print("Error: There was a problem with reading the file.")
    print("Please check that the file exists and that it is in a json format.")
    print("-- Technical Error Message -- ")
    print(e.__doc__)
    print(e.__str__())
finally:
    if not file.closed: #check if file is open
        file.close() #close file if file is open

# Present and Process the data
while True:

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha(): #check if user input is alphabets
                raise ValueError("The first name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha(): #check if user input is alphabets
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e: # to catch Value error i.e. if user input for first and last name is not alphabetic then it cannot be store if string variables
            print(e)  # Prints valueerror message stored in e
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e: # general exception handling for any other types of errors
            print("Error: There was a problem with your entered data.")
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print('-' * 50)
        for student in students: # run loop for as many rows of student data in students 2 D list - students
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-"*50)
        continue

    # Save the data to a file
    # On menu choice 3, the program opens a file named "Enrollments.json" in write mode using the open() function.
    # It writes the content of the students variable to the file using the dump() function,
    # then file is closed using the close() method. Then displays what was stored in the file.
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            file.close()
            print('The following student data was saved to file: ')
            for student in students:
                print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        except Exception as e:
            if file.closed == False:
                file.close()
            print('Error: There was a problem with writing to the file.')
            print('-- Technical Error Message -- ')
            print(e.__doc__)
            print(e.__str__())
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
