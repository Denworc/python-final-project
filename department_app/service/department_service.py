from department_app import db
from department_app.models import Department


class DepartmentService:

    @staticmethod
    def get_departments_list():
        return Department.query.order_by(Department.id).all()

    @staticmethod
    def get_department(department_id):
        return Department.query.get_or_404(department_id)

    @staticmethod
    def get_department_by_name(name):
        return Department.query.filter_by(name=name).first()

    @staticmethod
    def add_department(name):
        department = Department(name=name)

        db.session.add(department)
        db.session.commit()

    @staticmethod
    def update_department(department_id, name):
        department = Department.query.get_or_404(department_id)
        department.name = name

        db.session.commit()

    @staticmethod
    def delete_department(department_id):
        department = Department.query.get_or_404(department_id)

        db.session.delete(department)
        db.session.commit()
