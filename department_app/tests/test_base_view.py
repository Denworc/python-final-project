import http
from department_app.tests.tests import BaseCase


class EmployeeViewTestCase(BaseCase):
    def test_index_view(self):
        response = self.client.get('/')
        assert response.status_code == http.HTTPStatus.OK
        response = self.client.get('/home')
        assert response.status_code == http.HTTPStatus.OK
