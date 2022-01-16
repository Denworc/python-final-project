"""
    Employee model used to represent employees
"""
from department_app import db


class Employee(db.Model):
    """
        Model representing employee
    :param name: employee's name
    :param date_of_birth: employee's date of birth
    :param salary: employee's salary
    :param department_id: employee`s department
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey("department.id"))
    date_of_birth = db.Column(db.Date, nullable=False)
    salary = db.Column(db.Integer)

    def __init__(self, name, date_of_birth, salary=0, department_id=None):
        """
            Employee initialization
        :param name: employee's name
        :param date_of_birth: employee's date of birth
        :param salary: employee's salary
        :param department_id: employee`s department
        """
        self.name = name
        self.department_id = department_id
        self.date_of_birth = date_of_birth
        self.salary = salary

    def __repr__(self):
        """
            Returns string representation of employee
        :return: employee`s name
        """
        return self.name
