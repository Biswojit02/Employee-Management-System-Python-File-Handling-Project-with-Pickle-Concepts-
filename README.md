# 🧑‍💼 Employee Management System (Python)
A modular and file-based Employee Management System built using Python, demonstrating core programming concepts like:

- File Handling using pickle
- Modular Programming
- Custom Exception Handling
- Input Validation
- CRUD Operations (Create, Read, Update, Delete)
---

## 🚀 Features


- ✅ Add new employee records
- ✅ Delete employee records
- ✅ Update employee details
- ✅ View single employee
- ✅ View all employees
- ✅ Search employee by ID
- ✅ Name validation with custom exceptions
- ✅ Prevent duplicate employee IDs
---

## 🛠️ Technologies Used


- Python 
- File Handling (pickle)
- Custom Exception Handling
- Modular Programming
---

## 📁 Project Structure

```
Employee-Management-System/
│
├── File System/
|   └── File.txt
|
├── EmployeeMenu.py               # Menu UI
├── EmployeeAdd.py                # Add employee
├── EmployeeDelete.py             # Delete employee
├── EmployeeUpdate.py             # Update employee
├── EmployeeView.py               # View employee(s)
├── EmployeeSearch.py             # Search employee
├── EmployeeMainProject.py        # Main entry point
│
└── EmpNameValidation/            # Validation package
    ├── NameValidException.py
    └── NameValidateOperation.py

```
---

## ▶️ How to Run


1. Clone the repository:
git clone https://github.com/Biswojit02/employee-management-system.git

2. Navigate to the project folder:
cd employee-management-system

3. Run the main file:
python EmployeeMainProject.py

---

## 💡 How It Works


- Employee data is stored in a binary file: Employee.info
- Uses pickle to serialize and deserialize Python objects
- Each employee record is stored as a dictionary
- File is read using loop until EOFError

---

## 🧠 Key Concepts Demonstrated


- Python File Handling
- Exception Handling (Built-in + Custom)
- Data Validation
- Looping & Control Flow
- Modular Code Design

---

## ⚠️ Error Handling


- Invalid ID input (non-numeric)
- File not found
- Invalid name (empty, spaces, special characters)

---

## 🔥 Future Improvements


- Add GUI (Tkinter / Web App)
- Use Database (SQLite / MySQL)
- Add Login System
- Export data to CSV/Excel
- Auto-generate Employee IDs

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repo and submit a pull request.

---

## 📜 License

This project is open-source and available under the MIT License.

---

⭐ If you like this project, don't forget to star the repository!
