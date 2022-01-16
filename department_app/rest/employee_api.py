from datetime import datetime

from flask import Flask, request
from flask_restful import Resource, Api, reqparse, abort, fields, marshal_with
from department_app import api
from department_app import service


def abort_if_todo_doesnt_exist(employee_id):
    """

    :param employee_id:
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

    """
    @staticmethod
    @marshal_with(resource_fields, envelope='departments')
    def get(id=0):
        """

        :param id:
        :return:
        """
        if id == 0:
            return service.EmployeeService.get_employees_list(), 200
        abort_if_todo_doesnt_exist(id)
        return service.EmployeeService.get_employee(id), 200

    @staticmethod
    def post():
        """

        :return:
        """
        params = parser.parse_args()
        params['date_of_birth'] = datetime.strptime(params['date_of_birth'], '%Y-%m-%d')
        service.EmployeeService.add_employee(params)
        return 'Created successfully', 201

    @staticmethod
    def put(id):
        """

        :param id:
        :return:
        """
        params = parser.parse_args()
        params['date_of_birth'] = datetime.strptime(params['date_of_birth'], '%Y-%m-%d')
        service.EmployeeService.update_employee(id, params)
        return 'Edited successfully', 201

    @staticmethod
    def delete(id):
        """

        :param id:
        :return:
        """
        abort_if_todo_doesnt_exist(id)
        service.EmployeeService.delete_employee(id)
        return 'Deleted successfully', 204


api.add_resource(EmployeesApi, "/api/v1/employees", "/api/v1/employees/", "/api/v1/employees/<int:id>")
