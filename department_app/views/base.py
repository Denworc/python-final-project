from flask import render_template
from department_app import app
from department_app import models


@app.route('/')
@app.route('/home')
def index():
    departments = models.Department.query.order_by(models.Department.id).all()
    return render_template("index.html", departments=departments)
