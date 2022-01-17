"""
Module contains '/departments' route handling functions.
Functions:
    departments()
    department(id)
    department_delete(id):
"""
from flask import render_template, url_for, redirect, flash
from department_app import app
from department_app import forms, service, rest


@app.route('/departments', methods=['POST', 'GET'])
def departments():
    """
        Function display departments list and take parameters to add new department by POST request
    :return: Departments page template
    """
    form = forms.DepartmentForm()

    if form.validate_on_submit():
        if service.DepartmentService.get_department_by_name(name=form.name.data):
            flash('Department {} already exist'.format(
                form.name.data))
            return redirect(url_for('departments'))
        try:
            service.DepartmentService.add_department(name=form.name.data)
            flash('You add new department: {}'.format(
                form.name.data))
            return redirect(url_for('departments'))
        except Exception as ex:
            return str(ex)

    departments = service.DepartmentService.get_departments_list()
    return render_template("departments.html", content='<h1>Main page<h1>', departments=departments, form=form)


@app.route('/departments/<int:id>', methods=['POST', 'GET'])
def department(id):
    """
        Function display department(id) page and take parameters to add new employee by POST request
    :param id:
    :return: Departments page template
    """
    department = service.DepartmentService.get_department(id)
    departments = service.DepartmentService.get_departments_list()
    form = forms.EmployeeForm()

    if department:
        form.department_id.data = department.id
    else:
        form.department_id.data = None
    form.department_id.choices = [(int(d.id), d.name) for d in departments]

    if form.validate_on_submit():
        data = {
            "name": form.name.data,
            "date_of_birth": form.date_of_birth.data,
            "salary": form.salary.data,
            "department_id": department.id
        }

        try:
            service.EmployeeService.add_employee(data)
            flash('You add new employee: {}'.format(
                form.name.data))
            return redirect(url_for('department', id=department.id))
        except Exception as ex:
            return str(ex)

    employees = department.employees

    return render_template("department.html", department=department, employees=employees, form=form)


@app.route('/departments/<int:id>/delete')
def department_delete(id):
    """
        Function delete department from db by id and redirect on departments page.
    :param id:
    :return: Departments page template
    """
    try:
        service.DepartmentService.delete_department(id)
        return redirect(url_for('departments'))
    except Exception as ex:
        return str(ex), 404
