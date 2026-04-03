/*
===================================================================================================
                           Employee Main File: Key Highlights
===================================================================================================

            1. Modular Employee Management System built using Python
            2. Implements full CRUD operations (Add, Delete, Update, View, Search)
            3. Uses pickle for efficient file-based data storage
            4. Menu-driven program with continuous loop execution
            5. Uses match-case (Python 3.10+) for clean decision handling
            6. Robust exception handling for invalid inputs and errors
            7. Follows separation of concerns with multiple modules
            8. Ensures smooth user interaction with validated inputs & error messages

===================================================================================================
*/




from EmployeeMenu import menu
from EmployeeAdd import add_employee
from EmployeeDelete import delete_employee
from EmployeeUpdate import update_employee
from EmployeeView import view_employee, view_all_employee
from EmployeeSearch import search_employee

while True:
    try:
        menu()
        ch=int(input("\tEnter your choice: "))
        match (ch):
            case 1:
                add_employee()
            case 2:
                delete_employee()
            case 3:
                update_employee()
            case 4:
                view_employee()
            case 5:
                view_all_employee()
            case 6:
                search_employee()
            case 7:
                print("Thank you for using this program.")
                break
            case _:
                print("Invalid choice. Please try again.")
    except ValueError:
        print("Don't Enter Alphanumeric, string, Symbols or special characters. Please try again.") 

