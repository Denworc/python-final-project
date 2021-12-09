from flask import Flask, render_template
from department_app import app


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html", content='<h1>Main page<h1>')


@app.route('/departments')
def departments():
    return render_template("departments.html", content='<h1>Main page<h1>')


@app.route('/department/<int:id>')
def department(id):
    return render_template("department.html", department_id=str(id))


@app.route('/employees')
def employees():
    return render_template("employees.html", content='<h1>Main page<h1>')


@app.route('/employee/<int:id>')
def employee(id):
    return render_template("employee.html", employee_id=str(id))
