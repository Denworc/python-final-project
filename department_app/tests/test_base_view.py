import http
from department_app.tests.tests import BaseCase


class EmployeeViewTestCase(BaseCase):
    def test_index_view(self):
        response1 = self.client.get('/')
        response2 = self.client.get('/home')
        assert response1.status_code == http.HTTPStatus.OK
        assert response2.status_code == http.HTTPStatus.OK
