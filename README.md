Pharmacy Management System
A simple Flask-based web application to manage pharmacy records, including tracking medicines, sales, and inventory. The system allows pharmacists to add medicines, process sales, and monitor stock levels. Data is stored in a SQLite database.

Features
Medicine Management

Add new medicines to the inventory with details such as name, price, and quantity.

Track the stock of each medicine and monitor when stock is running low.

Update medicine information (e.g., price or quantity) as needed.

Sales Management

Record sales transactions and update the stock accordingly.

Keep track of total sales and generate sales reports.

Inventory Management

Monitor the current stock of all medicines.

Receive alerts when stock is low.

View a detailed history of stock changes.

Supplier Management

Track suppliers from whom medicines are purchased.

Record the purchase dates and quantities from each supplier.

Search and Filtering

Search medicines by name, type, or price.

Filter and view sales by date range (daily, weekly, or monthly).

Technologies Used
Python

Flask

Flask-SQLAlchemy (for database integration)

SQLite

HTML

CSS

JavaScript

Getting Started
Prerequisites
Python 3.8 or higher

pip (Python package manager)

Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yomna813/pharmacy-management-system.git
cd pharmacy-management-system
Install required dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the application:

bash
Copy
Edit
python app.py
Access the application in your browser at:

plaintext
Copy
Edit
http://127.0.0.1:5000
Project Structure
plaintext
Copy
Edit
pharmacy-management-system/
│
├── app.py               # Main application file (Flask)
├── models.py            # Database models for Medicines, Sales, and Suppliers
├── templates/           # HTML templates for rendering pages
│   ├── index.html       # Home page displaying inventory and sales
│   ├── add_medicine.html # Page to add new medicines to the inventory
│   ├── sales.html       # Page to process sales and view sales history
│   ├── inventory.html   # Page to view and manage inventory
│   └── suppliers.html   # Page to manage supplier information
├── static/              # Static files (CSS, JavaScript, Images)
├── pharmacy.db          # SQLite database for storing medicines, sales, and suppliers
└── requirements.txt     # List of required Python packages
How It Works
Home Page
Navigate to the homepage where you can view the current inventory, total sales, and quick actions to add medicines, record sales, or manage suppliers.

Add Medicine
Use the "Add Medicine" form to input details about new medicines, including name, price, and quantity. This will update the database and the inventory.

Sales Management
On the "Sales" page, you can record each sale by selecting the medicine sold and the quantity. The stock is automatically updated.

Inventory Management
On the "Inventory" page, you can view all medicines in stock, update quantities, and monitor when stock levels are running low.

Supplier Management
Manage suppliers by adding details such as supplier name, contact information, and purchase history.

Search and Filter
You can search for medicines based on name, type, or price, and filter sales by different time ranges (daily, weekly, or monthly).

Future Improvements
Add user authentication for secure login (admin panel for pharmacy managers).

Implement advanced inventory tracking with low-stock alerts.

Generate sales reports and export them as CSV or PDF.

Integrate barcode scanning for sales processing.

License
This project is licensed under the MIT License.

Project Flow Overview:
Homepage: Displays an overview of the current stock, recent sales, and quick links to add new medicines, record sales, or manage suppliers.

Add Medicines: Forms to add new medicines, update stock, and track expiration dates.

Sales and Inventory Tracking: Track sales in real-time and update inventory accordingly.

Supplier Details: Keep track of where each medicine is sourced from, including cost and delivery dates.
