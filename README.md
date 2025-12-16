# e_learning_lms (minimal)

This is a minimal Django-based E-Learning LMS scaffold using SQLite.

How to use:
1. Create a virtualenv and activate it.
2. Install requirements: `pip install -r requirements.txt`
3. Run migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Create a superuser:
   ```
   python manage.py createsuperuser
   ```
5. Run server:
   ```
   python manage.py runserver
   ```
