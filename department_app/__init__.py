import os
import logging
from logging.handlers import RotatingFileHandler

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config


# def create_app(test_config=None):
#     """Application-factory pattern"""
#     app = Flask(__name__, instance_relative_config=True)
#     app.config.from_mapping(
#         SECRET_KEY='some_dev_key',
#         # DATABASE=os.path.join(app.instance_path, 'department_app.sqlite'),
#         SQLALCHEMY_DATABASE_URI='sqlite:///app.db',
#         SQLALCHEMY_TRACK_MODIFICATIONS=False
#     )
#     db = SQLAlchemy(app)
#
#     if test_config is None:
#         # load the instance config, if it exists, when not testing
#         app.config.from_pyfile('config.py', silent=True)
#     else:
#         # load the test config if passed in
#         app.config.from_mapping(test_config)
#
#         # ensure the instance folder exists
#     try:
#         os.makedirs(app.instance_path)
#     except OSError:
#         pass
#
#     return app


app = Flask(__name__, instance_relative_config=True)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)





# import logger
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




# if test_config is None:
#     # load the instance config, if it exists, when not testing
#     app.config.from_pyfile('config.py', silent=True)
# else:
#     # load the test config if passed in
#     app.config.from_mapping(test_config)

    # ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass


# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)





# from department_app.views import views
from department_app import views
