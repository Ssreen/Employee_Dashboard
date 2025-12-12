 Employee Dashboard – Django Project

A simple Employee Directory web application built with the Django framework.
This project allows users to create, read, update, and delete (CRUD) employee records.
It also includes a built-in search function and uses Django’s ORM and templating system.

✨ Features

✔ Add new employees

✔ View all employees in a directory-style list

✔ Edit or update employee details

✔ Delete employees

✔ Search employees by id

✔ Uses Django ModelForms

✔ SQLite database (default)

✔ Clean and minimal UI (HTML + optional Bootstrap)

🛠️ Tech Stack
Component	Technology
Backend	Django 4+
Frontend	HTML, Django Templates (Bootstrap optional)
Database	SQLite
Language	Python 3.10+


Each employee record contains:

First Name

Last Name

Email

Phone

Department

These fields can be extended easily in models.py.

 How the App Works
🔹 List Employees

Displays all employees using a table.

🔹 Add Employee

Uses Django ModelForm to create new employee records.

🔹 Edit Employee

Loads the selected employee into a pre-filled form.

🔹 Delete Employee

Removes the employee permanently.
