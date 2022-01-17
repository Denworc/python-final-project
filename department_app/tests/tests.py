"""

"""
import http
from datetime import datetime, timedelta
from flask import current_app
import unittest
from department_app import app, db
from config import Config, TestingConfig
# from department_app.models import Department, Employee

# client = app.test_client()


class BaseCase(unittest.TestCase):
    """

    """
    def setUp(self):
        """
        Execute before every test case
        :return:
        """
        self.app = app
        app.config.from_object(TestingConfig)
        self.client = app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        """
        Execute after every test case
        :return:
        """
        db.session.remove()
        db.drop_all()

    # def test_department_add(self):
    #     res = self.client.get('/departments')
    #
    #     assert res.status_code == 200


class BaseViewTestCase(BaseCase):
    def test_index_view(self):
        """

        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)
        response = self.client.get('/home')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)


class DepartmentViewTestCase(BaseCase):
    def test_departments(self):
        """

        """
        response = self.client.get('/departments')
        assert response.status_code == http.HTTPStatus.OK
        response = self.client.get('/home')
        assert response.status_code == http.HTTPStatus.OK

    def test_department(self):
        """

        """
        response = self.client.get('/departments')
        assert response.status_code == http.HTTPStatus.OK
        response = self.client.get('/home')
        assert response.status_code == http.HTTPStatus.OK

    def test_department_delete(self):
        """

        """
        response = self.client.get('/departments')
        assert response.status_code == http.HTTPStatus.OK
        response = self.client.get('/home')
        assert response.status_code == http.HTTPStatus.OK


class EmployeeViewTestCase(BaseCase):
    def test_index_view(self):
        """

        """
        response1 = self.client.get('/')
        response2 = self.client.get('/home')
        assert response1.status_code == http.HTTPStatus.OK
        assert response2.status_code == http.HTTPStatus.OK


class ErrorViewTestCase(BaseCase):
    def test_index_view(self):
        """

        """
        response1 = self.client.get('/')
        response2 = self.client.get('/home')
        assert response1.status_code == http.HTTPStatus.OK
        assert response2.status_code == http.HTTPStatus.OK


if __name__ == '__main__':
    unittest.main()
