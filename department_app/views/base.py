"""
Module contains '/home' route handling functions.
Functions:
    index()
"""
from flask import render_template
from department_app import app
from department_app import models, service


@app.route('/')
@app.route('/home')
def index():
    """
        Function display main page of application with departments and employees lists.
    :return: Main page template
    """
    employees = service.EmployeeService.get_employees_list()
    departments = service.DepartmentService.get_departments_list()
    return render_template("index.html", departments=departments, employees=employees)
