from datetime import datetime, timedelta
import unittest
from .. import app, db
# from department_app.models import Department, Employee


class DepartmentModelCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_department_add(self):
        pass
