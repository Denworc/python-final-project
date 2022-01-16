"""
    Functions / classes to work with department table (CRUD operations)
"""
from department_app import db
from department_app.models import Department


class DepartmentService:
    """
    Department service class for CRUD operations
    """
    @staticmethod
    def get_departments_list():
        """
            Function return departments list from db
        :return: departments list
        """
        return Department.query.order_by(Department.id).all()

    @staticmethod
    def get_department(department_id):
        """
            Function return department by id from db
        :param department_id: department`s id
        :return: department with given id
        """
        return Department.query.get_or_404(department_id)

    @staticmethod
    def get_department_by_name(name):
        """
            Function return department by name from db
        :param name: department`s name
        :return: department with given name
        """
        return Department.query.filter_by(name=name).first()

    @staticmethod
    def add_department(name):
        """
            Function add department to db
        :param name: department`s name
        :return: None
        """
        department = Department(name=name)

        db.session.add(department)
        db.session.commit()

    @staticmethod
    def update_department(department_id, name):
        """
            Function update department by id
        :param department_id: department`s id
        :param name: department`s name.
        :return: None
        """
        department = Department.query.get_or_404(department_id)
        department.name = name

        db.session.commit()

    @staticmethod
    def delete_department(department_id):
        """
            Function delete department by id from db
        :param department_id: department`s id
        :return: None
        """
        department = Department.query.get_or_404(department_id)

        db.session.delete(department)
        db.session.commit()
