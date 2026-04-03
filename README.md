# 🧑‍💼 Employee Management System (Python)
A modular and file-based Employee Management System built using Python, demonstrating core programming concepts like:

- File Handling using pickle
- Modular Programming
- Custom Exception Handling
- Input Validation
- CRUD Operations (Create, Read, Update, Delete)
---

## ⚙️ Features

| Feature | Description |
|---|---|
| ➕ Add Employee | Add new employee with ID, Name, Salary, Company |
| 🗑️ Delete Employee | Delete employee record by ID |
| ✏️ Update Employee | Update Salary and Company of existing employee |
| 👁️ View Employee | View a single employee record by ID |
| 📋 View All Employees | Display all stored employee records |
| 🔍 Search Employee | Search and verify employee by ID |
| ✅ Name Validation | Custom validation for employee and company names |
| 🚨 Custom Exceptions | Handles zero length, spaces, and invalid name errors |

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
├── EmployeeMainFile.py        # Main entry point
│
└── EmpNameValidation/            # Validation package
    ├── NameValidException.py
    └── NameValidateOperation.py

```
---

## 🧩 Modules Overview

### `EmployeeMainFile.py`
- Entry point of the application
- Uses `match-case` (Python 3.10+) for menu-driven control flow
- Imports all modules and calls respective functions

### `EmployeeMenu.py`
- Contains `menu()` function
- Displays the main menu to the user

### `EmployeeAdd.py`
- `is_unique(employee)` — checks if employee ID already exists
- `add_employee()` — collects data, validates, and saves using `pickle`

### `EmployeeDelete.py`
- `delete_employee()` — finds and removes employee record by ID

### `EmployeeUpdate.py`
- `update_employee()` — updates Salary and Company of an employee

### `EmployeeView.py`
- `view_employee()` — displays a single employee's details
- `view_all_employee()` — displays all employee records in table format

### `EmployeeSearch.py`
- `search_employee()` — searches for an employee by ID and confirms existence

### `Emp&CompNameValidation/` (Package)
- **`NameValidException.py`** — defines 3 custom exceptions:
  - `ZeroNameLengthError` — raised when name is empty
  - `SpaceError` — raised when name contains only spaces
  - `InvalidNameError` — raised when name has numbers/symbols
- **`NameValidateOperation.py`** — contains `name_validate()` function that
  validates employee and company names using above exceptions

---

## 🗃️ Data Storage

- Records are stored in **`Employee.info`** binary file
- Uses Python's **`pickle`** module for serialization
- Each record is stored as a **dictionary**:

\`\`\`python
{
    "ID"     : 101,
    "Name"   : "Rahul Kumar",
    "Salary" : 50000.00,
    "Company": "TechCorp"
}
\`\`\`

---

## ▶️ How to Run


**1. Clone the repository**
\`\`\`bash
git clone https://github.com/Biswojit02/employee-information-system.git
cd employee-information-system
\`\`\`

**2. Update the path in `EmployeeAdd.py` and `EmployeeUpdate.py`**
\`\`\`python
sys.path.append("your/local/path/to/Emp&CompNameValidation")
\`\`\`

**3. Run the main program**
\`\`\`bash
python EmployeeMainFile.py
\`\`\`

---

## 📋 Requirements

- Python **3.10+** (for `match-case` support)
- No external libraries required
- Uses only built-in modules: `pickle`, `sys`

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

This project is licensed under the **MIT License**.  
Feel free to use, modify, and distribute.

---


⭐ If you like this project, don't forget to star the repository!
