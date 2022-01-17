from datetime import datetime
from department_app import db
from department_app import service
from department_app.models import Employee
from department_app.tests.tests import BaseCase


class EmployeeServiceTestCase(BaseCase):
    def test_get_employee_list(self):
        employee = Employee(name="test",
                            date_of_birth=datetime.strptime('1999-01-01', '%Y-%m-%d'),
                            salary=123,
                            department_id=1,
                            )

        db.session.add(employee)
        db.session.commit()

        self.assertEqual(1, len(service.EmployeeService.get_employees_list()))

    def test_get_employee(self):
        employee = Employee(name="test",
                            date_of_birth=datetime.strptime('1999-01-01', '%Y-%m-%d'),
                            salary=123,
                            department_id=1,
                            )

        db.session.add(employee)
        db.session.commit()
        self.assertEqual(1, service.EmployeeService.get_employee(1).id)

    def test_get_employee_by_date(self):
        start_date = datetime.strptime('1995-01-01', '%Y-%m-%d')
        end_date = datetime.strptime('1997-01-01', '%Y-%m-%d')
        end_date_2 = datetime.strptime('2001-01-01', '%Y-%m-%d')
        employee = Employee(name="test",
                            date_of_birth=datetime.strptime('1999-01-01', '%Y-%m-%d'),
                            salary=123,
                            department_id=1,
                            )

        db.session.add(employee)
        db.session.commit()
        self.assertNotEqual(service.EmployeeService.get_employees_by_date(start_date, end_date_2),
                            service.EmployeeService.get_employees_by_date(start_date, end_date))
        self.assertEqual(1, len(service.EmployeeService.get_employees_by_date(start_date, end_date_2)))

    def test_add_employee(self):
        data = {
            "name": "test",
            "date_of_birth": datetime.strptime('1999-01-01', '%Y-%m-%d'),
            "salary": 123,
            "department_id": 1
        }
        service.EmployeeService.add_employee(data)
        self.assertEqual(1, Employee.query.count())

    def test_update_employee(self):
        data = {
            "name": "new_name",
            "date_of_birth": datetime.strptime('1999-01-01', '%Y-%m-%d'),
            "salary": 123,
            "department_id": 1
        }
        employee = Employee(name="test",
                            date_of_birth=datetime.strptime('1999-01-01', '%Y-%m-%d'),
                            salary=123,
                            department_id=1,
                            )

        db.session.add(employee)
        db.session.commit()

        service.EmployeeService.update_employee(1, data)
        self.assertEqual("new_name", str(Employee.query.get(1)))

    def test_delete_employee(self):
        employee = Employee(name="test",
                            date_of_birth=datetime.strptime('1999-01-01', '%Y-%m-%d'),
                            salary=123,
                            department_id=1,
                            )

        db.session.add(employee)
        db.session.commit()

        service.EmployeeService.delete_employee(1)
        self.assertEqual(0, Employee.query.count())
