"""
Module contains error handling functions.
Functions:
    not_found_error(error)
    internal_error(error)
"""
from flask import render_template
from department_app import app, db


@app.errorhandler(404)
def not_found_error(error):
    """
        Function for 404 error handling
    :param error: error code
    :return: 404 error page template
    """
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    """
       Function for 500 error handling
    :param error: error code
    :return: 500 error page template
    """
    db.session.rollback()
    return render_template('errors/500.html'), 500
