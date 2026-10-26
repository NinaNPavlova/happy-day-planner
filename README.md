# Happy Day Planner

A small Django web application for keeping track of the celebrations of the
people you care about: birthdays, name days and other special occasions, plus
the gifts you plan to give them. The home page shows a monthly calendar with
the celebrations marked on it.

Built as the individual project for the **Django Basics** course @ SoftUni.

## Features

- **Calendar home page** with month navigation (previous / next month) and an
  icon for every celebration (birthday, name day, other).
- **Celebrations**: create, list, view details. The list can be **filtered by
  type** and **sorted by title**.
- **People**: full CRUD. Each person can be linked to one or more celebrations
  and shows their age (calculated from the year of birth).
- **Gifts**: full CRUD. Each gift belongs to one person; the same gift cannot
  be added twice for the same person.
- Confirmation page before deleting a person or a gift.
- Custom 404 page.
- Responsive layout built with Bootstrap 5.

## Tech stack

- Python 3.13
- Django 6.1
- SQLite
- Bootstrap 5 (loaded from a CDN)

## Project structure

```
happy-day-planner/
├── config/          # project settings and root urls
├── celebrations/    # Celebration model, forms, views, home calendar
├── contacts/        # Person model, forms, views, custom template filter
├── gifts/           # Gift model, forms, views
├── templates/       # base template, partials and page templates
├── static/          # CSS
├── manage.py
└── requirements.txt
```

## Database models

| Model | App | Fields |
|-------|-----|--------|
| `Celebration` | celebrations | `celebration_type` (birthday / name day / other), `title`, `day_of_month`, `month` |
| `Person` | contacts | `name`, `surname`, `phone`, `year_of_birth`, `celebrations` |
| `Gift` | gifts | `person`, `gift` |

Relationships:

- `Person` ↔ `Celebration`: **many-to-many**.
- `Gift` → `Person`: **many-to-one** (a person can have many gifts).

## Validation

- A celebration of type "Other" must have a title.
- Day of month must be between 1 and 31, month between 1 and 12.
- Phone numbers are validated with a regular expression.
- A person cannot have the same gift twice (database constraint with a
  user-friendly error message).
- When editing a gift, the person field is read-only (disabled).

## Custom template filter

`person_age` (in `contacts/templatetags/contact_extras.py`) calculates a
person's age from their year of birth and returns `unknown` when the year is
missing or invalid.

## Getting started

1. Clone the repository and open the project folder:

   ```bash
   git clone https://github.com/NinaNPavlova/happy-day-planner.git
   cd happy-day-planner
   ```

2. Create and activate a virtual environment.

   Windows (PowerShell):

   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

   Linux / macOS:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply the database migrations:

   ```bash
   python manage.py migrate
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

6. Open <http://127.0.0.1:8000/> in your browser.

## Environment variables

No environment variables or credentials are needed. The project runs with its
default settings and uses a local SQLite database (`db.sqlite3`), which is
created when you run the migrations. The database starts empty: all data is
created through the application's interface.

## How to try it

1. Open **Celebrations** → **Add celebration** and create a birthday (for
   example 15 / 3).
2. Open **People** → **Add person**, fill in the details and tick the
   celebration you just created.
3. Open **Gifts** → **Add gift** and choose the person.
4. Go back to the **Home** page and open the month of your celebration to see
   it on the calendar.

Authentication and user management are intentionally not part of this project.