"""
    Module with RESTful service implementation of employee elements
"""
from datetime import datetime

from flask_restful import Resource, reqparse, abort, fields, marshal_with
from department_app import api
from department_app import service


def abort_if_todo_doesnt_exist(employee_id):
    """
        Function check element in db by id
    :param employee_id: employee`s id
    """
    try:
        service.EmployeeService.get_employee(employee_id)
    except:
        abort(404, message="Employee doesn't exist")


parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('date_of_birth')
parser.add_argument('salary')
parser.add_argument('department_id')

resource_fields = {
    'id': fields.String,
    'name': fields.String,
    'date_of_birth': fields.DateTime(dt_format='iso8601'),
    'salary': fields.Integer,
    'department_id': fields.Integer,
}


class EmployeesApi(Resource):
    """
        Employees Api service implementation class
    """
    @staticmethod
    @marshal_with(resource_fields, envelope='departments')
    def get(id=0):
        """
            Function return employee by id or employees list
        :param id: employee`s id
        :return: employee / employees list
        """
        if id == 0:
            return service.EmployeeService.get_employees_list(), 200
        abort_if_todo_doesnt_exist(id)
        return service.EmployeeService.get_employee(id), 200

    @staticmethod
    def post():
        """
            Function ad new employee element to db
        :return: {message}, 201
        """
        params = parser.parse_args()
        params['date_of_birth'] = datetime.strptime(params['date_of_birth'], '%Y-%m-%d')
        service.EmployeeService.add_employee(params)
        return 'Created successfully', 201

    @staticmethod
    def put(id):
        """
            Function edit employee by id
        :param id: employee`s id
        :return: {message}, 201
        """
        params = parser.parse_args()
        params['date_of_birth'] = datetime.strptime(params['date_of_birth'], '%Y-%m-%d')
        service.EmployeeService.update_employee(id, params)
        return 'Edited successfully', 201

    @staticmethod
    def delete(id):
        """
            Function delete employee by id
        :param id: employee`s id
        :return: {message}, 204
        """
        abort_if_todo_doesnt_exist(id)
        service.EmployeeService.delete_employee(id)
        return 'Deleted successfully', 204


api.add_resource(EmployeesApi, "/api/v1/employees", "/api/v1/employees/", "/api/v1/employees/<int:id>")
