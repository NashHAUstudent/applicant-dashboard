# Job Applicant Dashboard

This is a Django web application designed to serve as a Job Applicant Dashboard for the "Junior Developer" position. It allows administrators to manage applicant information, view their portfolios, and delete applicant records.

## Features

* **Applicant Listing:** A dashboard view showing all applicants for the "Junior Developer" position (first name, last name, email).
* **Portfolio Management:** Create and manage applicant portfolios and associated projects via the Django Admin.
* **User Integration:** Utilizes Django's built-in User model for applicant information.
* **Detailed Portfolio View:** A dedicated page to view an applicant's full portfolio and their submitted projects.
* **Applicant Deletion:** Functionality to delete an applicant, which also removes their associated portfolio and projects.
* **Bootstrap Styling:** Uses Bootstrap for a clean and responsive user interface, served as a local static CDN.

## Project Structure

my_applicant_dashboard/
├── my_applicant_dashboard/
│   ├── settings.py
│   ├── urls.py  (Main project URL configurations)
│   └── ...
├── portfolio/            (Django app for portfolio management)
│   ├── models.py         (Portfolio and Project models)
│   ├── views.py          (Function-based and Class-based views)
│   ├── urls.py           (App-specific URL configurations)
│   ├── templates/
│   │   └── portfolio/    (HTML templates for list, detail, delete)
│   └── ...
├── static/               (Directory for Bootstrap CSS/JS)
│   └── bootstrap/
│       ├── css/
│       └── js/
├── templates/            (Base HTML templates)
│   └── base.html
├── manage.py
├── README.md
├── .gitignore
└── db.sqlite3            (Local development database - excluded from Git)
└── venv/                 (Python virtual environment - excluded from Git)