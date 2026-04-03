/*
=========================================================================================
                      Employee Search Module – Key Points
========================================================================================

            1. Searches employee records using Employee ID input
            2. Uses pickle file handling to read binary data from Employee.info
            3. Implements loop-based record traversal until end of file (EOFError)
            4. Validates existence of employee and displays confirmation message
            5. Uses flag (found) mechanism to track search result
            6. Handles invalid input (non-numeric ID) using ValueError
            7. Handles missing file scenario using FileNotFoundError
            8. Efficiently stops search using break once record is found
              
=========================================================================================
*/
import pickle

def search_employee():
    try:
        emp_id = int(input("Enter employee id to search: "))
        with open("Employee.info", "rb") as ed:
            found = False
            while True:
                try:
                    record = pickle.load(ed)
                    if record["ID"] == emp_id:
                        print("-" * 80)
                        print(f"\tEmployee found with ID:{emp_id} And Employee Name: {record['Name']}. Valid Employee")
                        print("-" * 80)
                        found = True
                        break
                except EOFError:
                    break
            if not found:
                print(f"Employee not found with ID: {emp_id}. Try Again!")
    except ValueError:
        print("Don't Enter Alphanumeric, string, Symbols or special characters for Employee ID. Please try again.")
    except FileNotFoundError:
        print("No employee records found. Please add employees first.")
