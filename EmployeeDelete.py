/*
=============================================================================================
                    Delete Employee Module – Key Features
=============================================================================================
                      
        1. Deletes employee record using unique Employee ID
        2. Reads all records from binary file using pickle
        3. Stores data temporarily in a list for processing
        4. Searches for matching Employee ID efficiently
        5. Removes the record using list pop() method
        6. Rewrites updated data back to file (wb mode)
        7. Handles case when employee ID is not found
        8. Includes error handling for missing file (FileNotFoundError)
                              
=============================================================================================
*/


import pickle
def delete_employee():
    try:
        with open("Employee.info", "rb") as ed:
            emp_id = int(input("Enter employee id to delete: "))
            found = False
            records = []
            while True:
                try:
                    record = pickle.load(ed)
                    records.append(record)
                except EOFError:
                    break
        for index in range(len(records)):
            if records[index]["ID"] == emp_id:
                found = True
                recindex=index
                break
        if found:
            records.pop(recindex)
            with open("Employee.info", "wb") as ed:
                for record in records:
                    pickle.dump(record, ed)
            print("Employee record has been deleted successfully.You must Verify the deleted record by using view employee option.")
        else:
            print("Employee with the specified ID not found.")
    except FileNotFoundError:
        print("File not found. Please Check the file name and try again.")
