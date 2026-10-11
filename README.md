# Campus Placement & Recruitment Portal

## 1. Project Overview

The **Campus Placement & Recruitment Portal** is a database-driven web application developed to organize and manage campus recruitment activities. It provides a centralized platform for viewing student records, company details, job opportunities, and placement information.

The project demonstrates the practical application of Database Management System (DBMS) concepts through relational database design, SQL, primary keys, foreign keys, and integration of a MySQL database with a Flask web application.

## 2. Objectives

- Maintain student and company information in a centralized database.
- Organize job opportunities offered by recruiting companies.
- Store student applications and job eligibility criteria.
- Track placement records and package details.
- Establish relationships between database tables using primary and foreign keys.
- Develop a web interface to display database records.

## 3. Features

- Dashboard for navigating the portal.
- Student records display.
- Company information display.
- Job listings with job details.
- Placement records display.
- MySQL database connectivity through Flask.
- Relational database design with nine tables.
- EER diagram documenting the database structure.

## 4. Technology Stack

| Component | Technology |
|---|---|
| Frontend | HTML, CSS, Jinja2 templates |
| Backend | Python, Flask |
| Database | MySQL |
| Database connectivity | MySQL Connector/Python |
| Environment configuration | python-dotenv |
| Database design | MySQL Workbench |
| Version control | Git and GitHub |

## 5. Database Design

The database, named `mydb`, contains the following nine tables:

| Table | Purpose |
|---|---|
| `admin` | Stores administrator-related information |
| `student` | Stores student details |
| `company` | Stores recruiting company information |
| `job` | Stores job openings and recruitment criteria |
| `application` | Records student applications for jobs |
| `eligibility` | Stores job eligibility criteria |
| `skill` | Maintains a list of skills |
| `student_skill` | Connects students with their skills |
| `placement` | Stores placement outcomes and related details |

### Database Relationships

- A company can offer multiple jobs.
- Students can apply for jobs through application records.
- Applications connect students and jobs.
- Eligibility records are associated with jobs.
- The `student_skill` table represents the relationship between students and skills.
- Placement records are linked to relevant students, companies, and applications.

Primary keys uniquely identify records, while foreign keys maintain referential integrity between related tables.

The EER diagram is included in the repository to illustrate the database structure and relationships.

## 6. Project Structure

```text
CampusPlacementPortal/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── EER diagram.mwb
├── EER diagram.png
└── templates/
    └── HTML template files
```

The `.env` file, Python virtual environment, and local database backup are excluded from Git version control to avoid exposing credentials and unnecessary local files.

## 7. Prerequisites

Before running the application, install:

- Python 3
- MySQL Server
- MySQL Workbench (recommended)
- Git (optional, for cloning the repository)

## 8. Installation and Setup

### Step 1: Clone the repository

```bash
git clone https://github.com/sahanam30-design/CampusPlacementPortal.git
cd CampusPlacementPortal
```

Alternatively, download the repository as a ZIP file from GitHub.

### Step 2: Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Step 3: Install dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 4: Configure the MySQL database

1. Install and start MySQL Server.
2. Create or restore the `mydb` database and its nine tables.
3. Ensure that the required primary keys, foreign keys, and application data are configured.
4. Create a local `.env` file in the project root and configure the MySQL credentials expected by `app.py`.

**Important:** Replace example credentials with your own local settings. Never publish your MySQL password, `.env` file, or sensitive database records in a public repository.

The local database backup is not included in this public repository. Database setup or backup files should be shared separately when required by the academic submission guidelines.

### Step 5: Run the application

```bash
python app.py
```

### Step 6: Open the portal

Open the following address in Google Chrome:

http://127.0.0.1:5000/

Ensure that MySQL Server is running and the database connection settings are correct.

## 9. Application Routes

| Page | Route |
|---|---|
| Dashboard | `/` |
| Students | `/students` |
| Companies | `/companies` |
| Jobs | `/jobs` |
| Placements | `/placements` |

## 10. Future Enhancements

- Student and administrator authentication.
- Online job application submission.
- Automated eligibility verification.
- Search and filtering of students and job listings.
- Create, update, and delete operations for authorized users.
- Placement statistics and graphical reports.
- Improved validation and error handling.

## 11. Academic Significance

This third-year DBMS academic project demonstrates relational database design, SQL, primary and foreign key constraints, entity relationships, and database integration with a Python Flask web application.

It provides a practical example of connecting database concepts with a web-based application.

## 12. Repository

GitHub: https://github.com/sahanam30-design/CampusPlacementPortal
