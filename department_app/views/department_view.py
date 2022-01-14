from flask import Flask, render_template, url_for, request, redirect, flash, current_app
from department_app import app, db
from department_app import models, errors, forms


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
    employees = department.employees.all()

    if request.method == 'POST':
        pass
    else:
        return render_template("department.html", department=department, employees=employees)


@app.route('/department/<int:id>/delete')
def department_delete(id):
        department = models.Department.query.get_or_404(id)

        try:
            db.session.delete(department)
            db.session.commit()
            return redirect(url_for('departments'))
        except:
            return "DB_DEL_ERROR"
