
[![Build Status](https://app.travis-ci.com/Denworc/python-final-project.svg?branch=main)](https://app.travis-ci.com/Denworc/python-final-project)
[![Coverage Status](https://coveralls.io/repos/github/Denworc/python-final-project/badge.svg?branch=main)](https://coveralls.io/github/Denworc/python-final-project?branch=main)

# EPAM Online Python external program (final project): Department app
***
Simple web application for managing departments and employees. 
The web application use aforementioned web service for storing data and reading from database.

The web application allow:

1. display a list of departments and the average salary (calculated automatically) for these departments
2. display a list of employees in the departments with an indication of the salary for each employee and a search field to search for employees born on a certain date or in the period between dates 
3. change (add / edit / delete) the above data
***
### Deployment

1. Create the virtual environment: 
```html

    cd python-final-project

    python -m venv env

    source venv/bin/activate

```
2. Install requirements:
```html

    pip install -r requirements.txt

```
3. Run the migration:
```html

    flask db init
    
    flask db migrate
    
    flask db upgrade

```
4. Run the application:
   1. With gunicorn (available on : http://127.0.0.1:8000):
```html

    gunicorn app:app

```
   2. With flask development server (available on : http://127.0.0.1:5000/):
```html

    flask run

```
***




