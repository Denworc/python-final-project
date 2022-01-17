import http
from datetime import datetime, timedelta
import unittest
from department_app import app, db
from department_app import service, rest
from config import Config, TestingConfig
from department_app.models import Department, Employee
from department_app.tests.tests import BaseCase


class DepartmentAPITestCase(BaseCase):
    def test_department_get_method(self):
        response = self.client.get('/api/v1.0/departments')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)
        response = self.client.get('/api/v1.0/departments/')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)
        response = self.client.get('/api/v1.0/departments/1')
        self.assertEqual(response.status_code, http.HTTPStatus.NOT_FOUND)
        department = Department(name="test")
        db.session.add(department)
        db.session.commit()
        response = self.client.get('/api/v1.0/departments/1')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_department_post_method(self):
        response = self.client.post('/api/v1.0/departments', data=dict(name='test'), follow_redirects=True)
        self.assertEqual(response.status_code, http.HTTPStatus.CREATED)

    def test_department_put_method(self):
        department = Department(name="test")
        db.session.add(department)
        db.session.commit()
        response = self.client.put('/api/v1.0/departments/1', data=dict(name='new_name'), follow_redirects=True)
        self.assertEqual(response.status_code, http.HTTPStatus.CREATED)
        self.assertEqual('new_name', str(Department.query.get(1)))

    def test_department_delete_method(self):
        department = Department(name="test")
        db.session.add(department)
        db.session.commit()
        response = self.client.delete('/api/v1.0/departments/1')
        self.assertEqual(response.status_code, http.HTTPStatus.NO_CONTENT)

