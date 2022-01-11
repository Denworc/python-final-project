from flask import Flask, render_template, url_for, request, redirect
from department_app import app, Department, db


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html", content='<h1>Main page<h1>')


@app.route('/departments', methods=['POST', 'GET'])
def departments():
    if request.method == 'POST':
        name = request.form['name']

        department = Department(name=name)

        try:
            db.session.add(department)
            db.session.commit()
            return redirect('/departments')
        except:
            return "DB_ADD_ERROR"
    else:
        departments = Department.query.order_by(Department.id).all()
        return render_template("departments.html", content='<h1>Main page<h1>', departments=departments)


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
            return redirect('/departments')
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
