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


 How to Use

ADmin pass i used
Login: Admin
Pass: 20993591

Admin Panel:
Visit /admin and log in using your superuser credentials.

Add Users via Django’s built-in User model.

Create Portfolios and link them to Users.

Add Projects and assign them to Portfolios.

Dashboard List View (Homepage):
htt*p://127.0.0.1:8000/ – Shows list of all applicants.

Applicant Detail View:
htt*p://127.0.0.1:8000/portfolio/<username>/ – View detailed portfolio.

Delete Applicant:
htt*p://127.0.0.1:8000/portfolio/<username>/delete/ – Delete user and related data.

💡 Notes
 Bootstrap is self-hosted under /static/bootstrap/.

 Job Position (Junior Developer) is hardcoded in the dashboard.

 Uses Django’s built-in User model with Portfolio and Project relations.

 Clean commit messages used (feat:, fix:, wip:).

 Commit Convention
Prefix	Meaning
feat:	New feature implemented
wip:	Work in progress
fix:	Fixes to existing feature
bug:	Feature has a bug

⚠.gitignore
The project uses a .gitignore file that excludes:

venv/ (Virtual Environment)

db.sqlite3 (Database file)

 License
This project is for educational purposes only.

 Project Link
GitHub Repository: https://github.com/NashHAUstudent/applicant-dashboard
