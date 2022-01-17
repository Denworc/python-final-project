"""

"""
import os
import logging
from logging.handlers import RotatingFileHandler

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import DevelopmentConfig, ProductionConfig
from flask_restful import Api


app = Flask(__name__, instance_relative_config=True)
app.config.from_object(ProductionConfig)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)

if not app.debug:

    if not os.path.exists('logs'):
        os.mkdir('logs')

    file_handler = RotatingFileHandler('logs/department_app.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)  # DEBUG, INFO, WARNING, ERROR, CRITICAL

    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Departments app')


from department_app import views
from department_app.rest.department_api import DepartmentApi
from department_app.rest.employee_api import EmployeesApi
