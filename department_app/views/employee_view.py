from flask import Flask, render_template, url_for, request, redirect, flash, current_app
from department_app import app, db
from department_app import models, errors, forms


@app.route('/employees', methods=['POST', 'GET'])
def employees():
    form = forms.EmployeeForm()

    if form.validate_on_submit():
        employee = models.Employee(name=form.name.data)

        try:
            db.session.add(employee)
            db.session.commit()
            flash('You add new employee: {}'.format(
                form.name.data))
            return redirect(url_for('employees'))
        except:
            return "DB_ADD_ERROR"

    departments = models.Department.query.order_by(models.Department.id).all()
    form.department_id.data = [str(departments[0].id)]
    form.department_id.choices = [(d.id, d.name) for d in departments]

    employees = models.Employee.query.order_by(models.Employee.id).all()
    return render_template("employees.html", content='<h1>Main page<h1>', employees=employees,
                           departments=departments, form=form)


@app.route('/employee/<int:id>', methods=['POST', 'GET'])
def employee(id):
    if request.method == 'POST':
        pass
    else:
        return render_template("employee.html", employee_id=str(id))
