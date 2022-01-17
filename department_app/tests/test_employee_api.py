import http
from datetime import datetime, timedelta
import unittest
from department_app import app, db
from department_app import service, rest
from config import Config, TestingConfig
from department_app.models import Department, Employee
from department_app.tests.tests import BaseCase


class EmployeeAPITestCase(BaseCase):
    def test_employee_get_method(self):
        response = self.client.get('/api/v1.0/employees')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)
        response = self.client.get('/api/v1.0/employees/')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)
        response = self.client.get('/api/v1.0/employees/1')
        self.assertEqual(response.status_code, http.HTTPStatus.NOT_FOUND)
        employee = Employee(name="test",
                            date_of_birth=datetime.strptime('1999-01-01', '%Y-%m-%d'),
                            salary=123,
                            department_id=1,
                            )
        db.session.add(employee)
        db.session.commit()
        response = self.client.get('/api/v1.0/employees/1')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_employee_post_method(self):
        response = self.client.post('/api/v1.0/employees', data=dict(name='test',
                                                                     date_of_birth='1999-01-01',
                                                                     salary=123,
                                                                     department_id=1,
                                                                     ), follow_redirects=True)
        self.assertEqual(response.status_code, http.HTTPStatus.CREATED)

    def test_employee_put_method(self):
        employee = Employee(name="test",
                            date_of_birth=datetime.strptime('1999-01-01', '%Y-%m-%d'),
                            salary=123,
                            department_id=1,
                            )
        db.session.add(employee)
        db.session.commit()
        response = self.client.put('/api/v1.0/employees/1', data=dict(name='new_name',
                                                                      date_of_birth='1999-01-01',
                                                                      salary=123,
                                                                      department_id=1,
                                                                      ), follow_redirects=True)
        self.assertEqual(response.status_code, http.HTTPStatus.CREATED)
        self.assertEqual('new_name', str(Employee.query.get(1).name))

    def test_employee_delete_method(self):
        employee = Employee(name="test",
                            date_of_birth=datetime.strptime('1999-01-01', '%Y-%m-%d'),
                            salary=123,
                            department_id=1,
                            )
        db.session.add(employee)
        db.session.commit()
        response = self.client.delete('/api/v1.0/employees/1')
        self.assertEqual(response.status_code, http.HTTPStatus.NO_CONTENT)

