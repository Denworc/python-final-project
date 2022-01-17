"""
    Module with RESTful service implementation of department elements
"""
from flask_restful import Resource, reqparse, abort, fields, marshal_with
from department_app import api
from department_app import service


def abort_if_todo_doesnt_exist(department_id):
    """
        Function check element in db by id
    :param department_id: department`s id
    """
    try:
        service.DepartmentService.get_department(department_id)
    except:
        abort(404, message="Department doesn't exist")


parser = reqparse.RequestParser()
parser.add_argument('name')

resource_fields = {
    'id': fields.String,
    'name': fields.String,
}


class DepartmentApi(Resource):
    """
        Employees Api service implementation class
    """
    @staticmethod
    @marshal_with(resource_fields, envelope='departments')
    def get(id=0):
        """
            Function return department by id or departments list
        :param id: department`s id
        :return: department / departments list
        """
        if id == 0:
            return service.DepartmentService.get_departments_list(), 200
        abort_if_todo_doesnt_exist(id)
        return service.DepartmentService.get_department(id), 200

    @staticmethod
    def post():
        """
            Function ad new department element to db
        :return: {message}, 201
        """
        params = parser.parse_args()
        if service.DepartmentService.get_department_by_name(name=params['name']):
            abort(422, message="Department already exist")
        service.DepartmentService.add_department(params['name'])
        return 'Created successfully', 201

    @staticmethod
    def put(id):
        """
            Function edit department by id
        :param id: department`s id
        :return: {message}, 201
        """
        params = parser.parse_args()
        service.DepartmentService.update_department(id, params['name'])
        return 'Edited successfully', 201

    @staticmethod
    def delete(id):
        """
            Function delete department by id
        :param id: department`s id
        :return: {message}, 204
        """
        abort_if_todo_doesnt_exist(id)
        service.DepartmentService.delete_department(id)
        return 'Deleted successfully', 204


api.add_resource(DepartmentApi, "/api/v1.0/departments", "/api/v1.0/departments/", "/api/v1.0/departments/<int:id>")
