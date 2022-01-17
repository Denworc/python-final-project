from department_app import db
from department_app import service
from department_app.models import Department
from department_app.tests.tests import BaseCase


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
