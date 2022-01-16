from datetime import datetime, timedelta
import unittest
from department_app import app, db
# from department_app.models import Department, Employee

client = app.test_client()


class DepartmentModelCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    @staticmethod
    def test_department_add():
        res = client.get('/departments')

        assert res.status_code == 200
