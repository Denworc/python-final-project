import http
from department_app import db
from department_app.models import Department
from department_app.tests.tests import BaseCase


class DepartmentViewTestCase(BaseCase):
    def test_departments_view(self):
        response = self.client.get('/departments')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)
        response = self.client.post('/departments', data=dict(name='test'), follow_redirects=True)
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_department_view(self):
        response = self.client.get('/departments/1')
        self.assertNotEqual(response.status_code, http.HTTPStatus.OK)
        department = Department(name="test")

        db.session.add(department)
        db.session.commit()
        response = self.client.get('/departments/1')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_department_delete_view(self):
        response = self.client.get('/departments/1/delete')
        self.assertEqual(response.status_code, http.HTTPStatus.NOT_FOUND)
        department = Department(name="test")

        db.session.add(department)
        db.session.commit()
        response = self.client.get('/departments/1/delete')
        self.assertEqual(response.status_code, http.HTTPStatus.FOUND)
