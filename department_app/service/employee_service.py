from department_app import db
from department_app.models import Employee
from datetime import datetime

class EmployeeService:

    @staticmethod
    def get_employees_list():
        return Employee.query.order_by(Employee.id).all()

    @staticmethod
    def get_employee(employee_id):
        return Employee.query.get_or_404(employee_id)

    @staticmethod
    def add_employee(data):
        employee = Employee(name=data["name"],
                            date_of_birth=data["date_of_birth"],
                            salary=int(data["salary"]),
                            department_id=int(data["department_id"]),
                            )
        db.session.add(employee)
        db.session.commit()

    @staticmethod
    def update_employee(employee_id, data):
        employee = Employee.query.get_or_404(employee_id)

        employee.name = data["name"]
        employee.date_of_birth = data["date_of_birth"]
        employee.salary = int(data["salary"])
        employee.department_id = int(data["department_id"])

        db.session.commit()

    @staticmethod
    def delete_employee(employee_id):
        employee = Employee.query.get_or_404(employee_id)

        db.session.delete(employee)
        db.session.commit()

    @staticmethod
    def get_employees_by_date(start_date, end_date):
        employee = Employee.query.filter(Employee.date_of_birth.between(start_date, end_date))

        return employee
