📌 How to Use
Admin Panel:
Visit /admin and log in using your superuser credentials.

Add Users via Django’s built-in User model.

Create Portfolios and link them to Users.

Add Projects and assign them to Portfolios.

Dashboard List View (Homepage):
http://127.0.0.1:8000/ – Shows list of all applicants.

Applicant Detail View:
http://127.0.0.1:8000/portfolio/<username>/ – View detailed portfolio.

Delete Applicant:
http://127.0.0.1:8000/portfolio/<username>/delete/ – Delete user and related data.

💡 Notes
✅ Bootstrap is self-hosted under /static/bootstrap/.

✅ Job Position (Junior Developer) is hardcoded in the dashboard.

✅ Uses Django’s built-in User model with Portfolio and Project relations.

✅ Clean commit messages used (feat:, fix:, wip:).

📝 Commit Convention
Prefix	Meaning
feat:	New feature implemented
wip:	Work in progress
fix:	Fixes to existing feature
bug:	Feature has a bug

⚠️ .gitignore
The project uses a .gitignore file that excludes:

venv/ (Virtual Environment)

db.sqlite3 (Database file)

📄 License
This project is for educational purposes only.

🔗 Project Link
GitHub Repository: https://github.com/NashHAUstudent/applicant-dashboard
