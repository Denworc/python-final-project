[![Coverage Status](https://coveralls.io/repos/github/Denworc/python-final-project/badge.svg?branch=main)](https://coveralls.io/github/Denworc/python-final-project?branch=main)

# EPAM Online Python external program (final project): Department app
***

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





