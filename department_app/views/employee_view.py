from flask import render_template, url_for, redirect, flash
from department_app import app, db
from department_app import models, forms


@app.route('/employees', methods=['POST', 'GET'])
def employees():
    form = forms.EmployeeForm()

    departments = models.Department.query.order_by(models.Department.id).all()
    # if departments:
    #     form.department_id.data = [int(departments[0].id)]
    # else:
    #     form.department_id.data = None
    form.department_id.choices = [(int(d.id), d.name) for d in departments]
    if form.validate_on_submit():
        employee = models.Employee(name=form.name.data,
                                   date_of_birth=form.date_of_birth.data,
                                   salary=form.salary.data,
                                   department_id=form.department_id.data,
                                   )

        try:
            db.session.add(employee)
            db.session.commit()
            flash('You add new employee: {}'.format(
                form.name.data))
            return redirect(url_for('employees'))
        except Exception as ex:
            return str(ex)

    employees = models.Employee.query.order_by(models.Employee.id).all()
    return render_template("employees.html", content='<h1>Main page<h1>',
                           employees=employees, form=form)


@app.route('/employee/<int:id>', methods=['POST', 'GET'])
def employee(id):
    employee = models.Employee.query.get_or_404(id)
    departments = models.Department.query.order_by(models.Department.id).all()

    form = forms.EmployeeForm()
    form.department_id.choices = [(int(d.id), d.name) for d in departments]

    if form.validate_on_submit():
        employee.name = form.name.data
        employee.date_of_birth = form.date_of_birth.data
        employee.salary = form.salary.data
        employee.department_id = form.department_id.data

        try:
            db.session.commit()
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


@app.route('/employee/<int:id>/delete')
def employee_delete(id):
        employee = models.Employee.query.get_or_404(id)

        try:
            db.session.delete(employee)
            db.session.commit()
            return redirect(url_for('employees'))
        except Exception as ex:
            return str(ex)
