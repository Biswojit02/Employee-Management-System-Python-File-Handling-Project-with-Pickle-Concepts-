/*
====================================================================================================================
                                            Update Employee Module
===================================================================================================================

          1. Updates existing employee details using Employee ID
          2. Reads all records from file using pickle.load()
          3. Searches for matching ID using loop
          4. Allows updating salary and company name
          5. Applies name validation using custom validation module
          6. Stores updated records in a list and rewrites file (wb mode)
          7. Handles errors like invalid input, file not found, invalid names
          8. Displays success message or "Employee not found" accordingly

====================================================================================================================
*/



import pickle
from NameValidException import ZeroNameLengthError, SpaceError, InvalidNameError
from NameValidateOperation import name_validate


def update_employee():
    try:
        with open("Employee.info", "rb") as ed:
            emp_id = int(input("Enter employee id to update: "))
            found = False
            records = []
            while True:
                try:
                    record = pickle.load(ed)
                    if record["ID"] == emp_id:
                        print("-" * 80)
                        print(f"\tEmployee found with ID: \"{emp_id}\" And Employee Name: {record['Name']}")
                        print("-" * 80)
                        new_salary = float(input("Enter new employee salary: "))
                        new_company_name = input("Enter new employee company name: ")
                        new_company = name_validate(new_company_name)
                        record["Salary"] = new_salary
                        record["Company"] = new_company
                        found = True
                    records.append(record)
                except EOFError:
                    break
        if found:
            with open("Employee.info", "wb") as ed:
                for record in records:
                    pickle.dump(record, ed)
            print("Employee record has been updated successfully.You must Verify the updated record by using view employee option.")
        else:
            print("Employee with the specified ID not found.")
    except ValueError:
        print("Don't Enter Alphanumeric, string, Symbols or special characters for Employee ID or Salary. Please try again.")
    except FileNotFoundError:
        print("File not found. Please Check the file name and try again.")
    except ZeroNameLengthError:
        print("You must fill Employee Name/Company Name... Try Again!")
    except SpaceError:
        print("Don't enter any space For Employee Name/Company Name.... Try Again!")
    except InvalidNameError:
        print("Invalid Employee Name/Company Name... Try Again!")
