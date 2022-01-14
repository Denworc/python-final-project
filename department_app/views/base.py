from flask import Flask, render_template, url_for, request, redirect, flash, current_app
from department_app import app, db
from department_app import models, errors, forms


@app.route('/')
@app.route('/home')
def index():
    departments = models.Department.query.order_by(models.Department.id).all()
    return render_template("index.html", departments=departments)
