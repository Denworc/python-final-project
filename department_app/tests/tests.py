import http
from datetime import datetime, timedelta
import unittest
from department_app import app, db
from department_app import service
from config import Config, TestingConfig
from department_app.models import Department, Employee


class BaseCase(unittest.TestCase):
    def setUp(self):
        self.app = app
        app.config.from_object(TestingConfig)
        self.client = app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class BaseViewTestCase(BaseCase):
    def test_index_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)
        response = self.client.get('/home')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)


class DepartmentServiceTestCase(BaseCase):
    def test_get_departments_list(self):
        department = Department(name="test")

        db.session.add(department)
        db.session.commit()

        self.assertEqual(1, len(service.DepartmentService.get_departments_list()))

    def test_get_department(self):
        department = Department(name="test")

        db.session.add(department)
        db.session.commit()
        self.assertEqual(1, service.DepartmentService.get_department(1).id)

    def test_get_department_by_name(self):
        department = Department(name="test")

        db.session.add(department)
        db.session.commit()
        self.assertEqual("test", service.DepartmentService.get_department_by_name("test").name)

    def test_add_department(self):
        service.DepartmentService.add_department(name="test")
        self.assertEqual(1, Department.query.count())

    def test_update_department(self):
        department = Department(name="test")

        db.session.add(department)
        db.session.commit()
        service.DepartmentService.update_department(1, "new_name")
        self.assertEqual("new_name", str(Department.query.get(1)))

    def test_delete_department(self):
        department = Department(name="test")

        db.session.add(department)
        db.session.commit()
        service.DepartmentService.delete_department(1)
        self.assertEqual(0, Department.query.count())


class DepartmentViewTestCase(BaseCase):
    def test_departments(self):
        response = self.client.get('/departments')
        assert response.status_code == http.HTTPStatus.OK

    def test_department(self):
        response = self.client.get('/departments')
        assert response.status_code == http.HTTPStatus.OK
        response = self.client.get('/home')
        assert response.status_code == http.HTTPStatus.OK

    def test_department_delete(self):
        response = self.client.get('/departments')
        assert response.status_code == http.HTTPStatus.OK
        response = self.client.get('/home')
        assert response.status_code == http.HTTPStatus.OK


class EmployeeViewTestCase(BaseCase):
    def test_index_view(self):
        response1 = self.client.get('/')
        response2 = self.client.get('/home')
        assert response1.status_code == http.HTTPStatus.OK
        assert response2.status_code == http.HTTPStatus.OK


class ErrorViewTestCase(BaseCase):
    def test_index_view(self):
        response1 = self.client.get('/')
        response2 = self.client.get('/home')
        assert response1.status_code == http.HTTPStatus.OK
        assert response2.status_code == http.HTTPStatus.OK


if __name__ == '__main__':
    unittest.main()
