# Hangarin

## Project Description

Hangarin is a web application built with Django that helps users organize their daily tasks, manage priorities, add notes, and break down large goals into smaller subtasks. It provides a clean, dashboard-driven interface with Google OAuth authentication and full CRUD support across all task-related entities.

## Features

- **Dashboard Overview** — Live summary cards showing total tasks, completed, pending, in-progress, subtasks, and notes count, with category and priority breakdowns.
- **Full CRUD Support** — Create, read, update, and delete records across all entities: Tasks, SubTasks, Notes, Categories, and Priorities.
- **Search Functionality** — Search across all list views by relevant fields (e.g., task title, description, category, priority, note content).
- **Filtering** — Filter Tasks independently by status, priority, and category with active filter pills. Filter SubTasks by status only.
- **Sorting** — Sort Notes by newest first or oldest first based on creation date.
- **Pagination** — All list views are paginated (5 records per page) for easier navigation of large datasets.
- **Admin Panel** — Enhanced Django admin interface with search, filtering, and display customization for all models.
- **Google OAuth** — Sign in with Google in addition to the standard username/email and password login.
- **Seed Data** — Faker-based management command to populate the database with sample tasks, notes, and subtasks.

## Data Models

| Model | Description |
|---|---|
| Priority | Priority level for a task (e.g., High, Medium, Low, Critical, Optional) |
| Category | Category label for a task (e.g., Work, School, Personal, Finance, Projects) |
| Task | Main to-do item with title, description, deadline, status, category, and priority |
| Note | Text note linked to a specific task |
| SubTask | Child task linked to a parent task with its own status |

## Tech Stack

- **Backend:** Django 5.1.4 (Python)
- **Database:** SQLite
- **Frontend:** Bootstrap 4, jQuery, Ready Admin Theme (olive-themed)
- **Auth:** django-allauth (Google OAuth 2.0)
- **Other:** django-widget-tweaks, Faker (for seed data), PyJWT, cryptography

## Installation

1. Clone the repository.
```bash
   git clone https://github.com/ihlay/Hangarin.git
   cd Hangarin
```

2. Create and activate a virtual environment.
```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # Mac / Linux
```

3. Install dependencies.
```bash
   pip install -r requirements.txt
```

4. Apply migrations.
```bash
   cd projectsite
   python manage.py migrate
```

5. Create a superuser.
```bash
   python manage.py createsuperuser
```

6. (Optional) Load initial seed data.
```bash
   python manage.py populate_data
```

7. Run the development server.
```bash
   python manage.py runserver
```

## Author

**Eli Karl Torres Arnejo**
arnejoelikarl@gmail.com