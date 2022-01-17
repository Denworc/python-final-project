from department_app.tests.tests import BaseCase


class EmployeeServiceTestCase(BaseCase):
    def test_not_found_error(self):
        path = '/non_existent_endpoint'
        response = self.client.get(path)
        self.assertEqual(response.status_code, 404)
