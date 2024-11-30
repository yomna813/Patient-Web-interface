# Python
Patient Management System
A simple Flask-based web application to manage patient records. The system allows users to sign up with their details and search for patient records using a National ID. Data is stored in a SQLite database.

Features
Patient Signup

Users can register their details including name, email, National ID, and birthdate.
Password validation ensures security, and data is checked for duplicates before being stored.
Patient Search

Search for patient records using their National ID.
Displays user information including username, email, and National ID.
SQLite Database Integration

Patient data is stored in a lightweight SQLite database.
Form Validation

Form inputs are validated using WTForms, ensuring data integrity.

Technologies Used
Python
Flask
Flask-WTF
SQLite
HTML

How It Works
Main Page
Navigate to the homepage.

Signup
Fill out the signup form with required details. On successful submission, the data is added to the database.

Search
Enter a valid National ID to search for a patient. If found, the user details are displayed.

Validation

All fields are required.
Password and confirm password must match.
Duplicate National IDs are rejected.

How It Works
Main Page
Navigate to the homepage.

Signup
Fill out the signup form with required details. On successful submission, the data is added to the database.

Search
Enter a valid National ID to search for a patient. If found, the user details are displayed.

Validation

All fields are required.
Password and confirm password must match.
Duplicate National IDs are rejected.



