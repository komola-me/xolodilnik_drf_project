# VegeFoods (Clone)

A backend-only e-commerce application inspired by VegeFoods, built with Django, Django REST Framework, PostgreSQL, Celery, Redis, and JWT authentication. Designed for learning and demonstration purposes.

## Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/komola-me/xolodilnik_drf_project.git
   cd xolodilnik_drf_project
   ```

2. Use the package manager [uv](https://docs.astral.sh/uv/getting-started/installation/) to install dependencies.

3. Create Virtual Environment and install dependencies:
   ```bash
   uv init
   uv venv # creates virtual environment
   .venv\Scripts\activate # activates virtual environment
   uv sync # installs all dependencies
   ```

4. Set up environment variables:
   - Duplicate .env.example as .env
   - Fill in settings such as DB_NAME, SECRET_KEY, ...


## Usage
1. Apply database migrations:
   ```bash
   python manage.py migrate
   ```
2. Run the Django development server:
   ```bash
   python manage.py runserver
   ```
   Your API should now be running locally at http://127.0.0.1:8000/.



## 💡 Author
Made with 💙 by [komola-me]
For educational purposes only