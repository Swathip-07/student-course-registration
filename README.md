**Pala Swathi Ezu - Django Project**

A Django-based web application that allows students to register for courses and manage their enrollments.

What this project contains

**Main app:** `courseinfo`  
**Project package:** `pala_swathi_ezu`  
Key features implemented:
- CRUD for Instructors, Courses, Semesters (Year+Period), Sections and Students.
- Student `Registration` model linking a `Student` to a `Section`.
- Class-based views (List, Detail, Create, Update, Delete) with login & permission mixins.
- Admin registration for all models.
- Basic templates and CSS in `courseinfo/templates/courseinfo` and `courseinfo/static/courseinfo`.

## Tools and Technologies

- **Python 3.8+** — Programming language
- **Django 3.2** — Web framework
- **SQLite** — Default local database for development
- **Git** — Version control system
- **GitHub** — Code hosting platform
- **HTML,CSS** — Frontend styling


Getting Started (Local Development)

Prerequisites:
- Python 3.8+
- PostgreSQL (optional for local if you want to test Postgres, else SQLite is default)

Installation:
1. Clone the repository:
   git clone https://github.com/Swathip-07/student-course-registration.git
   cd student-course-registration

2. Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate

3. Install dependencies:
   pip install -r requirements.txt

4. Apply migrations
python manage.py makemigrations
python manage.py migrate

5. Create a superuser (admin)
python manage.py createsuperuser

6. Run the development server
python manage.py runserver
Open: http://127.0.0.1:8000/

Author & Contact

Made by Swathi P

Contact: swathip200467@gmail.com

---

