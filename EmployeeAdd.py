/*
===================================================================================

      1. Adds new employee records using file handling (pickle)
      2. Ensures unique Employee ID using is_unique() validation
      3. Implements custom name validation (only alphabets allowed)
      4. Handles multiple exceptions (invalid input, empty name, file errors)
      5. Uses loop to allow multiple employee entries in one run
      6. Stores data in binary file (Employee.info) as dictionaries
      7. Follows modular design with separate validation package
      8. Ensures data consistency and prevents duplicate records

===================================================================================

*/



import pickle
import sys

sys.path.append(
    "D:\\PYTHON\ADVANCE PY\\5. Employee Information System\\EmpNameValidation"
)  # Add parent directory to the system path
from NameValidException import ZeroNameLengthError, SpaceError, InvalidNameError
from NameValidateOperation import name_validate


def is_unique(employee):
    try:
        with open("Employee.info", "rb") as ed:
            found=True
            records = []
            
            while True:
                try:
                    record = pickle.load(ed)
                    records.append(record)
                except EOFError:
                    break
            
            for record in records:
                if record["ID"] == employee["ID"]:
                    found=False
                    break
            return found
            
    except FileNotFoundError:
        print("File not found. Please Check the file name and try again.")



def add_employee():
    with open("Employee.info", "ab") as ed:
        while True:
            try:
                print("-" * 60)
                emp_id = int(input("Enter employee id: "))
                name = input("Enter employee name: ")
                emp_name = name_validate(name)
                emp_salary = float(input("Enter employee salary: "))
                company = input("Enter employee company name: ")
                emp_company = name_validate(company)
                employee = {
                    "ID": emp_id,
                    "Name": emp_name,
                    "Salary": round(emp_salary, 2),
                    "Company": emp_company,
                }
                if is_unique(employee):
                    pickle.dump(employee, ed)
                    print("Employee data saved as record into file successfully.")
                else:
                    print("Employee ID already exists. Please try again with a unique ID.")
                choice = input("Do you want to add more employee records? (yes/no): ")
                if choice.lower() != "yes":
                    break
            except ValueError:
                print(
                    "Don't Enter Alphanumeric, string, Symbols or special characters for Employee ID or Salary. Please try again."
                )
            except ZeroNameLengthError:
                print("You must fill Employee Name/Company Name... Try Again!")
            except SpaceError:
                print(
                    "Don't enter any space For Employee Name/Company Name.... Try Again!"
                )
            except InvalidNameError:
                print("Invalid Employee Name/Company Name... Try Again!")
