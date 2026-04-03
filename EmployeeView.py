/*
=========================================================================================================
                             Employee View Module: Key features
=========================================================================================================

        1. View specific employee details using Employee ID
        2. Display all employee records in structured format
        3. Reads data from binary file using pickle
        4. Uses loop with EOFError to read all records safely
        5. Implements search logic for matching employee ID
        6. Handles invalid input using ValueError
        7. Handles missing file using FileNotFoundError
        8. Displays formatted output for better readability
=========================================================================================================

*/

import pickle

def view_employee():
    try:
        emp_id = int(input("Enter employee id to view: "))
        with open("Employee.info", "rb") as ed:
            found = False
            while True:
                try:
                    record = pickle.load(ed)
                    if record["ID"] == emp_id:
                        print("-" * 80)
                        print("\t\tEmployee Information:")
                        print("-" * 80)
                        print(f"\tEmp ID: {record['ID']}")
                        print(f"\tEmp Name: {record['Name']}")
                        print(f"\tEmp Salary: {record['Salary']}")
                        print(f"\tCompany: {record['Company']}")
                        found = True
                        break
                except EOFError:
                    break
            if not found:
                print(f"No employee found with ID: {emp_id}")
    except ValueError:
        print("Don't Enter Alphanumeric, string, Symbols or special characters for Employee ID. Please try again.")
    except FileNotFoundError:
        print("No employee records found. Please add employees first.")

def view_all_employee():
    try:
        with open("Employee.info", "rb") as ed:
            print("-" * 80)
            print("\t\tAll Employee Information:")
            print("-" * 80)
            print("\tEmp ID\t\tEmp Name\tEmp Salary\t\tCompany")
            while True:
                try:
                    record = pickle.load(ed)
                    print(f"\t{record['ID']}\t\t{record['Name']}\t\t{record['Salary']}\t\t\t{record['Company']}")
                except EOFError:
                    break
    except FileNotFoundError:
        print("No employee records found. Please add employees first.")
