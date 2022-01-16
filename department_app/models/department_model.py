"""
    Department model used to represent departments
"""
from department_app import db


class Department(db.Model):
    """
        Model representing department
    :param name: department`s name
    :param employees: employees in department
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    employees = db.relationship('Employee', cascade="all,delete", backref='department', lazy='select')

    def __init__(self, name, employees=None):
        """
            Employee initialization
        :param name: employee`s name
        :param employees:
        """
        self.name = name
        self.employees = employees if employees is not None else []

    def get_average_salar(self):
        """
            Function calculates average salary for department
        :return: average_salary
        """
        if self.employees:
            return sum(map(lambda employee: employee.salary, self.employees)) // len(self.employees)
        return 0

    def __repr__(self):
        """
            Returns string representation of department
        :return: department`s name
        """
        return self.name
