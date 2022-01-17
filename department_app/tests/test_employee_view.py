import http
from datetime import datetime, timedelta
import unittest
from department_app import app, db
from department_app import service
from config import Config, TestingConfig
from department_app.models import Department, Employee
from department_app.tests.tests import BaseCase


class EmployeeViewTestCase(BaseCase):
    def test_employees_view(self):
        response = self.client.get('/employees')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)
        response = self.client.post('/employees', data=dict(name='test'), follow_redirects=True)
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_employee_view(self):
        response = self.client.get('/employees/1')
        self.assertNotEqual(response.status_code, http.HTTPStatus.OK)
        employee = Employee(name="test",
                            date_of_birth=datetime.strptime('1999-01-01', '%Y-%m-%d'),
                            salary=123,
                            department_id=1,
                            )

        db.session.add(employee)
        db.session.commit()
        response = self.client.get('/employees/1')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_employee_delete_view(self):
        response = self.client.get('/employees/1/delete')
        self.assertEqual(response.status_code, http.HTTPStatus.NOT_FOUND)
        employee = Employee(name="test",
                            date_of_birth=datetime.strptime('1999-01-01', '%Y-%m-%d'),
                            salary=123,
                            department_id=1,
                            )

        db.session.add(employee)
        db.session.commit()
        response = self.client.get('/employees/1/delete')
        self.assertEqual(response.status_code, http.HTTPStatus.FOUND)
