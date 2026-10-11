
import os
from pathlib import Path

import mysql.connector
from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent / ".env", override=True)

app = Flask(__name__)


def get_db_connection():
    password = os.environ.get("MYSQL_PASSWORD")

    if not password:
        raise RuntimeError(
            "MYSQL_PASSWORD is missing. Check your .env file."
        )

    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=password,
        database="mydb"
    )


@app.route("/")
def home():
    connection = None

    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        stats = {}

        for table in ["student", "company", "job", "placement"]:
            cursor.execute(f"SELECT COUNT(*) AS total FROM `{table}`")
            stats[table] = cursor.fetchone()["total"]

        cursor.close()

        return render_template("index.html", stats=stats)

    except Exception:
        app.logger.exception("Unable to load dashboard")
        return (
            "<h2>Dashboard could not load</h2>"
            "<p>Check the Flask terminal for the error details.</p>"
            '<a href="/test-db">Test database connection</a>',
            500
        )

    finally:
        if connection is not None and connection.is_connected():
            connection.close()


@app.route("/test-db")
def test_db():
    connection = None

    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT DATABASE() AS db_name")
        result = cursor.fetchone()

        cursor.execute("SELECT COUNT(*) AS total FROM student")
        students = cursor.fetchone()["total"]

        cursor.execute("SELECT COUNT(*) AS total FROM company")
        companies = cursor.fetchone()["total"]

        cursor.execute("SELECT COUNT(*) AS total FROM job")
        jobs = cursor.fetchone()["total"]

        cursor.close()

        return render_template(
            "records.html",
            title="Database Connection Test",
            columns=["Item", "Value"],
            rows=[
                {"Item": "Database", "Value": result["db_name"]},
                {"Item": "Students", "Value": students},
                {"Item": "Companies", "Value": companies},
                {"Item": "Jobs", "Value": jobs},
            ]
        )

    except Exception:
        app.logger.exception("Database test failed")
        return (
            "<h2>Database test failed</h2>"
            "<p>Check the Flask terminal for details.</p>",
            500
        )

    finally:
        if connection is not None and connection.is_connected():
            connection.close()


def get_records(table, title):
    connection = None
    cursor = None

    allowed_tables = {
        "student",
        "company",
        "job",
        "placement"
    }

    if table not in allowed_tables:
        return "Invalid table name", 400

    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute(f"SELECT * FROM `{table}`")
        rows = cursor.fetchall()

        columns = [column[0] for column in cursor.description]

        return render_template(
            "records.html",
            title=title,
            columns=columns,
            rows=rows
        )

    except Exception:
        app.logger.exception("Failed to load %s", table)
        return (
            f"<h2>Unable to load {title}</h2>"
            "<p>Check the Flask terminal for details.</p>",
            500
        )

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None and connection.is_connected():
            connection.close()


@app.route("/students")
def students():
    return get_records("student", "Student Directory")


@app.route("/companies")
def companies():
    return get_records("company", "Recruiting Companies")


@app.route("/jobs")
def jobs():
    return get_records("job", "Job Opportunities")


@app.route("/placements")
def placements():
    return get_records("placement", "Placement Records")


if __name__ == "__main__":
    app.run(debug=True)
