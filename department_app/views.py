from flask import Flask, render_template, url_for, request, redirect, flash
from department_app import app, db
from department_app.models import Department
from department_app.forms.departmentForms import DepartmentForm


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html", content='<h1>Main page<h1>')


@app.route('/departments', methods=['POST', 'GET'])
def departments():
    form = DepartmentForm()

    if form.validate_on_submit():
        department = Department(name=form.name.data)

        try:
            db.session.add(department)
            db.session.commit()
            flash('You add new department: {}'.format(
                form.name.data))
            return redirect(url_for('departments'))
        except:
            return "DB_ADD_ERROR"

    if request.method == 'POST':
        name = request.form['name']

        department = Department(name=name)

        try:
            db.session.add(department)
            db.session.commit()
            return redirect(url_for('departments'))
        except:
            return "DB_ADD_ERROR"
    departments = Department.query.order_by(Department.id).all()
    return render_template("departments.html", content='<h1>Main page<h1>', departments=departments, form=form)


@app.route('/department/<int:id>', methods=['POST', 'GET'])
def department(id):
    if request.method == 'POST':
        pass
    else:
        department = Department.query.get(id)
        return render_template("department.html", department=department)


@app.route('/department/<int:id>/delete')
def department_delete(id):
        department = Department.query.get_or_404(id)

        try:
            db.session.delete(department)
            db.session.commit()
            return redirect(url_for('departments'))
        except:
            return "DB_DEL_ERROR"



@app.route('/employees', methods=['POST', 'GET'])
def employees():
    if request.method == 'POST':
        pass
    else:
        return render_template("employees.html", content='<h1>Main page<h1>')


@app.route('/employee/<int:id>', methods=['POST', 'GET'])
def employee(id):
    if request.method == 'POST':
        pass
    else:
        return render_template("employee.html", employee_id=str(id))
