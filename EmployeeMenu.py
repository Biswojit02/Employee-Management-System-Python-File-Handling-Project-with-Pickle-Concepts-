/*
=====================================================================================================
                             Employee Menu Module: Key features
=====================================================================================================

  Displays a structured menu interface for navigating different employee operations in the system.

      1. Displays the main user interface of the Employee Management System
      2. Provides 7 options for different operations:
           - Add Employee
           - Delete Employee
           - Update Employee
           - View Single Employee
           - View All Employees
           - Search Employee
           - Exit
      3. Uses formatted output ("=" * 60) to create a clean and structured layout
      4. Uses tab spacing (\t) for better alignment and readability
      5. Acts as a navigation hub for the entire application
      6. Does not take input — only responsible for displaying menu options
      7. Integrated with the main program to control flow using user choice
=====================================================================================================
  */



def menu():
    print("="*60)
    print("\t\tEmployee Information System")
    print("="*60)
    print("\t1. Add New Employee Information")
    print("\t2. Delete Employee Information")
    print("\t3. Update Employee Information")
    print("\t4. View Employee Information")
    print("\t5. View All Employees Information")
    print("\t6. Search Employee Information")
    print("\t7. Exit")
    print("="*60)
