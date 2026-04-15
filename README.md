# Portfolio Project

A personal portfolio website built with Django. The project includes a homepage, contact page, certificates page, custom static styling, and a downloadable resume.

## Features

- Personal portfolio homepage
- Contact page
- Certificates page
- Static CSS and JavaScript assets
- Resume PDF served from the `static` directory
- Simple Django project structure using template-based views

## Tech Stack

- Python
- Django 6
- HTML
- CSS
- JavaScript
- SQLite

## Project Structure

```text
viveek/
|-- manage.py
|-- requirements.txt
|-- runtime.txt
|-- portfolio/
|   |-- settings.py
|   |-- urls.py
|   |-- views.py
|   |-- wsgi.py
|   `-- asgi.py
|-- templates/
|   |-- base.html
|   |-- portfolio_v3.html
|   |-- contact.html
|   |-- certificates.html
|   `-- index.html
`-- static/
    |-- css/
    |   |-- main.css
    |   `-- styles.css
    |-- js/
    |   |-- script.js
    |   `-- responsive.js
    `-- resume/
        `-- Vivek_K_Resume.pdf
```

## Available Pages

- `/` - Portfolio homepage
- `/contact/` - Contact page
- `/certificates/` - Certificates page
- `/admin/` - Django admin panel

## Installation

1. Clone the repository:

```bash
git clone <your-repository-url>
cd viveek
```

2. Create and activate a virtual environment:

```bash
python -m venv selfenv
selfenv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run migrations:

```bash
python manage.py migrate
```

5. Start the development server:

```bash
python manage.py runserver
```

6. Open in your browser:

```text
http://127.0.0.1:8000/
```

## Requirements

The main dependencies used in this project are:

- Django==6.0.1
- asgiref==3.11.0
- sqlparse==0.5.5
- tzdata==2025.3

## Notes

- The project currently uses SQLite as the default database.
- Static files are configured through `STATICFILES_DIRS`.
- `DEBUG` is enabled in the current settings, which is suitable for development only.

## Future Improvements

- Add a working contact form with backend handling
- Improve SEO and metadata
- Add project sections with dynamic data
- Deploy the portfolio to a hosting platform
- Improve responsiveness and animations

## Author

Vivek Kumar Sharma
