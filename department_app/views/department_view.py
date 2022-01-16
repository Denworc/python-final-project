from flask import render_template, url_for, redirect, flash
from department_app import app, db
from department_app import models, forms, service


@app.route('/departments', methods=['POST', 'GET'])
def departments():
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

    departments = models.Department.query.order_by(models.Department.id).all()
    return render_template("departments.html", content='<h1>Main page<h1>', departments=departments, form=form)


@app.route('/departments/<int:id>', methods=['POST', 'GET'])
def department(id):
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
    try:
        service.DepartmentService.delete_department(id)
        return redirect(url_for('departments'))
    except:
        return "DB_DEL_ERROR"
