from flask import render_template, url_for, redirect, flash
from department_app import app, db
from department_app import models, forms, service


@app.route('/employees', methods=['POST', 'GET'])
def employees():
    form = forms.EmployeeForm()
    date_form = forms.EmployeeSearchForm()

    departments = service.DepartmentService.get_departments_list()
    form.department_id.choices = [(int(d.id), d.name) for d in departments]

    if date_form.validate_on_submit():
        employees = service.EmployeeService.get_employees_by_date(date_form.start_date.data, date_form.end_date.data)
        return render_template("employees.html", content='<h1>Main page<h1>',
                               employees=employees, form=form, date_form=date_form)

    if form.validate_on_submit():
        data = {
            "name": form.name.data,
            "date_of_birth": form.date_of_birth.data,
            "salary": form.salary.data,
            "department_id": form.department_id.data
        }

        try:
            service.EmployeeService.add_employee(data)
            flash('You add new employee: {}'.format(
                form.name.data))
            return redirect(url_for('employees'))
        except Exception as ex:
            return str(ex)

    employees = service.EmployeeService.get_employees_list()
    return render_template("employees.html", content='<h1>Main page<h1>',
                           employees=employees, form=form, date_form=date_form)


@app.route('/employees/<int:id>', methods=['POST', 'GET'])
def employee(id):
    employee = service.EmployeeService.get_employee(id)
    departments = service.EmployeeService.get_employees_list()

    form = forms.EmployeeForm()
    form.department_id.choices = [(int(d.id), d.name) for d in departments]

    if form.validate_on_submit():
        data = {
            "name": form.name.data,
            "date_of_birth": form.date_of_birth.data,
            "salary": form.salary.data,
            "department_id": form.department.id
        }

        try:
            service.EmployeeService.update_employee(id, data)
            flash('You change employee: {}'.format(
                form.name.data))
            return redirect(url_for('employees'))
        except Exception as ex:
            return str(ex)

    if departments:
        form.department_id.default = employee.department_id
    else:
        form.department_id.default = None
    form.process()

    return render_template("employee.html", employee=employee, form=form)


@app.route('/employees/<int:id>/delete')
def employee_delete(id):
    try:
        service.EmployeeService.delete_employee(id)
        return redirect(url_for('employees'))
    except Exception as ex:
        return str(ex)
