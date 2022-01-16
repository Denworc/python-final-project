"""
    Functions / classes to work with employee table (CRUD operations)
"""
from department_app import db
from department_app.models import Employee


class EmployeeService:
    """
    Employee service class for CRUD operations
    """
    @staticmethod
    def get_employees_list():
        """
            Function return employee list from db
        :return: employees list
        """
        return Employee.query.order_by(Employee.id).all()

    @staticmethod
    def get_employee(employee_id):
        """
            Function return employee by id from db
        :param employee_id: employee`s id
        :return: employee with given id
        """
        return Employee.query.get_or_404(employee_id)

    @staticmethod
    def add_employee(data):
        """
            Function add employee to db
        :param data: input data dict
        :return: None
        """
        employee = Employee(name=data["name"],
                            date_of_birth=data["date_of_birth"],
                            salary=int(data["salary"]),
                            department_id=int(data["department_id"]),
                            )
        db.session.add(employee)
        db.session.commit()

    @staticmethod
    def update_employee(employee_id, data):
        """
            Function update employee by id
        :param employee_id: employee`s id
        :param data: input data dict
        :return: None
        """
        employee = Employee.query.get_or_404(employee_id)

        employee.name = data["name"]
        employee.date_of_birth = data["date_of_birth"]
        employee.salary = int(data["salary"])
        employee.department_id = int(data["department_id"])

        db.session.commit()

    @staticmethod
    def delete_employee(employee_id):
        """
            Function delete employee by id from db
        :param employee_id: employee`s id
        :return: None
        """
        employee = Employee.query.get_or_404(employee_id)

        db.session.delete(employee)
        db.session.commit()

    @staticmethod
    def get_employees_by_date(start_date, end_date):
        """
            Function return employees in date range
        :param start_date: from 'date'
        :param end_date: to 'date'
        :return: employees list
        """
        employees = Employee.query.filter(Employee.date_of_birth.between(start_date, end_date))

        return employees
