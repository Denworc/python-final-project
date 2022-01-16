from flask import render_template
from department_app import app
from department_app import models, service


@app.route('/')
@app.route('/home')
def index():
    employees = service.EmployeeService.get_employees_list()
    departments = service.DepartmentService.get_departments_list()
    return render_template("index.html", departments=departments, employees=employees)
