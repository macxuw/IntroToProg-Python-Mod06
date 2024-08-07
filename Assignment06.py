# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   MClark,8/5/2024,input empty classes
#   MClark,8/5/2024,Filled class with functions
# ------------------------------------------------------------------------------------------ #
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
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
# student_first_name: str = ''  # Holds the first name of a student entered by the user.
# student_last_name: str = ''  # Holds the last name of a student entered by the user.
# course_name: str = ''  # Holds the name of a course entered by the user.
# json_data: str = ''  # Holds combined string data in a json format.
# file = None  # Holds a reference to an opened file.
# menu_choice: str  # Hold the choice made by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data


# Processing --------------------------------------- #
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files
    ChangeLog: (Who, When, What)
    MClark,8/5/2024,Created Class
    """
    # Read from the JSON file
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """
        This function reads JSON file data
        ChangeLog: (Who, When, What)
        MClark,8/5/2024,Created function
        :param file_name:
        :type file_name:
        :param student_data:
        :type student_data:
        :return:
        :rtype:
        """
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("This script requires an existing file! Initializing file.\n", e)
            file = open(FILE_NAME, "w")
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if not file.closed:
                file.close()
        return student_data

    # Saves JSON to file
    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """
        This function writes data to a JSON file
        ChangeLog: (Who, When, What)
        MClark,8/5/2024,Created function
        :param file_name:
        :type file_name:
        :param student_data:
        :type student_data:
        :return:student_data
        :rtype:
        """
        try:
            file = open(file_name, "w")
            json.dump(student_data, file, indent=1)
            file.close()
            print("The following data is saved:\n")
            print("*" * 40)
            for student in student_data:
                print(f"{student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}")
            print("*" * 40)
        except TypeError as e:
            IO.output_error_messages("File save requires a valid JSON format.", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if not file.closed:
                file.close()
        return student_data


# Presentation --------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    MClark,8/5/2024,Created Class
    MClark,8/5/2024, Added IO, display, and error functions
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays custom error messages
        ChangeLog: (Who, When, What)
        MClark,8/5/2024,Created function
        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    def output_menu(menu: str):
        """
        This function displays program menu
        ChangeLog: (Who, When, What)
        MClark,8/5/2024,Created function
        :return:
        :rtype:
        """
        print(menu)

    @staticmethod
    def input_menu_choice():
        """
        THis function takes the user's menu choice
        ChangeLog: (Who, When, What)
        MClark,8/5/2024,Created function
        :return:menu_choice
        """
        try:
            menu_choice = input("Enter your menu choice number: ").strip()
            if menu_choice not in ("1", "2", "3", "4"):  # Menu choices are string type
                raise Exception("Please choose an option from the menu.")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing e to avoid the technical message
        return menu_choice

    @staticmethod
    def output_student_courses(student_data: list):
        """
        Process the data to create and display a custom message
        ChangeLog: (Who, When, What)
        MClark,8/5/2024,Created function
        :param student_data:
        :type student_data:
        :return:
        :rtype:
        """
        print("-" * 50)
        for student in student_data:
            print(f"{student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}")
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """
        This function takes user input for student first and name and course name
        ChangeLog: (Who, When, What)
        MClark,8/5/2024,Created function
        :param student_data:
        :type student_data:
        :return: list
        :rtype:
        """
        try:
            student_first_name = input("Enter the student's \033[1mfirst name\033[0m: ").strip()
            if not student_first_name.isalpha() or len(student_first_name) < 2:
                raise ValueError("First name should only contain letters and be at least 2 characters.")

            student_last_name = input("Enter the student's \033[1mlast name\033[0m: ").strip()
            if not student_last_name.isalpha() or len(student_last_name) < 2:
                raise ValueError("Last name should only contain letters and be at least 2 characters.")

            course_name = input("Please enter the \033[1mcourse name\033[0m: ").strip()
            if not len(course_name) > 2:
                raise ValueError("Course name must be at least 3 characters.")
            student_data = {"FirstName": student_first_name, "LastName": student_last_name, "CourseName": course_name}
            students.append(student_data)
        # If inputs do not meet criteria, display error
        except ValueError as e:
            IO.output_error_messages(e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        return student_data


# Start script
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
while (True):

    # Present the menu of choices
    IO.output_menu(menu=MENU)
    # Process menu choice
    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_courses(student_data=students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop

print("Program Ended")
