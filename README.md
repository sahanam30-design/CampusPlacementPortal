\# Campus Placement \& Recruitment Portal



\## Project Overview



The Campus Placement \& Recruitment Portal is a database-driven web application designed to organize campus recruitment activities. It provides a centralized interface for viewing student details, company information, job opportunities, and placement records.



\## Objectives



\- Maintain student and company records.

\- Organize job opportunities offered by companies.

\- Store applications and eligibility information.

\- Track placement details.

\- Demonstrate relational database design and integration with a web application.



\## Features



\- Dashboard for navigating the portal.

\- Student records page.

\- Company records page.

\- Job listings page.

\- Placement records page.

\- MySQL database connectivity through Flask.



\## Technology Stack



\- \*\*Frontend:\*\* HTML and CSS with Jinja2 templates.

\- \*\*Backend:\*\* Python and Flask.

\- \*\*Database:\*\* MySQL.

\- \*\*Database connectivity:\*\* MySQL Connector/Python.

\- \*\*Environment configuration:\*\* python-dotenv.

\- \*\*Database design:\*\* MySQL Workbench EER diagram.

\- \*\*Version control:\*\* Git and GitHub.



\## Database Design



The database contains nine tables:



1\. `admin`

2\. `student`

3\. `company`

4\. `job`

5\. `application`

6\. `eligibility`

7\. `skill`

8\. `student\_skill`

9\. `placement`



Primary keys identify individual records, and foreign keys maintain relationships between related tables.



The EER diagram is included in this repository to document the database structure.



\## Project Structure



```text

CampusPlacementPortal/

├── app.py

├── requirements.txt

├── README.md

├── .gitignore

├── EER diagram.mwb

├── EER diagram.png

├── mydb\_backup.sql

└── templates/

```



The `.env` file and Python virtual environment are intentionally excluded from version control.



\## Prerequisites



\- Python 3

\- MySQL Server

\- MySQL Workbench (recommended for database inspection)

\- Git



\## Setup and Installation



1\. Clone or download this repository.

2\. Create and activate a Python virtual environment.

3\. Install dependencies:



&#x20;  ```bash

&#x20;  python -m pip install -r requirements.txt

&#x20;  ```



4\. Create or restore the MySQL database using the provided SQL backup, if needed.

5\. Configure the local `.env` file with your MySQL connection settings. Never commit passwords or other secrets.

6\. Start the application:



&#x20;  ```bash

&#x20;  python app.py

&#x20;  ```



7\. Open `http://127.0.0.1:5000/` in your browser.



\## Application Pages



\- Dashboard: `/`

\- Students: `/students`

\- Companies: `/companies`

\- Jobs: `/jobs`

\- Placements: `/placements`



\## Future Enhancements



\- Student and administrator login.

\- Online job application submission.

\- Automated eligibility checking.

\- Search, filtering, and record management.

\- Placement statistics and reports.



\## Academic Project



Developed as a third-year DBMS academic project to demonstrate relational database design, SQL, foreign-key relationships, and integration of a MySQL database with a Flask web application.

