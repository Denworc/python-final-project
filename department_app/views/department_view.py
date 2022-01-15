from flask import render_template, url_for, redirect, flash
from department_app import app, db
from department_app import models, forms


@app.route('/departments', methods=['POST', 'GET'])
def departments():
    form = forms.DepartmentForm()

    if form.validate_on_submit():
        department = models.Department(name=form.name.data)

        try:
            db.session.add(department)
            db.session.commit()
            flash('You add new department: {}'.format(
                form.name.data))
            return redirect(url_for('departments'))
        except:
            return "DB_ADD_ERROR"

    # if request.method == 'POST':
    #     name = request.form['name']
    #
    #     department = Department(name=name)
    #
    #     try:
    #         db.session.add(department)
    #         db.session.commit()
    #         return redirect(url_for('departments'))
    #     except:
    #         return "DB_ADD_ERROR"
    departments = models.Department.query.order_by(models.Department.id).all()
    return render_template("departments.html", content='<h1>Main page<h1>', departments=departments, form=form)


@app.route('/department/<int:id>', methods=['POST', 'GET'])
def department(id):
    department = models.Department.query.get_or_404(id)
    departments = models.Department.query.order_by(models.Department.id).all()
    form = forms.EmployeeForm()
    if department:
        form.department_id.data = department.id
    else:
        form.department_id.data = None
    form.department_id.choices = [(int(d.id), d.name) for d in departments]

    if form.validate_on_submit():
        employee = models.Employee(name=form.name.data,
                                   date_of_birth=form.date_of_birth.data,
                                   salary=form.salary.data,
                                   department_id=department.id
                                   )

        try:
            db.session.add(employee)
            db.session.commit()
            flash('You add new employee: {}'.format(
                form.name.data))
            return redirect(url_for('department', id=department.id))
        except Exception as ex:
            return str(ex)

    employees = department.employees

    return render_template("department.html", department=department, employees=employees, form=form)


@app.route('/department/<int:id>/delete')
def department_delete(id):
        department = models.Department.query.get_or_404(id)

        try:
            db.session.delete(department)
            db.session.commit()
            return redirect(url_for('departments'))
        except:
            return "DB_DEL_ERROR"
