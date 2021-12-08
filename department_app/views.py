from flask import Flask, render_template
from department_app import app


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/departments')
def departments():
    return 'Departments'


@app.route('/department/<int:id>')
def department(id):
    return 'Department #' + str(id)


@app.route('/employees')
def employees():
    return 'Employees'


@app.route('/employee/<int:id>')
def employee(id):
    return 'Employee #' + str(id)
