from flask import Flask, request
from flask_restful import Resource, Api, reqparse, abort, fields, marshal_with
from department_app import api
from department_app import service


def abort_if_todo_doesnt_exist(department_id):
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
    @staticmethod
    @marshal_with(resource_fields, envelope='departments')
    def get(id=0):
        if id == 0:
            return service.DepartmentService.get_departments_list(), 200
        abort_if_todo_doesnt_exist(id)
        return service.DepartmentService.get_department(id), 200

    @staticmethod
    def post():
        params = parser.parse_args()
        if service.DepartmentService.get_department_by_name(name=params['name']):
            abort(422, message="Department already exist")
        service.DepartmentService.add_department(params['name'])
        return 'Created successfully', 201

    @staticmethod
    def put(id):
        params = parser.parse_args()
        service.DepartmentService.update_department(id, params['name'])
        return 'Edited successfully', 201

    @staticmethod
    def delete(id):
        """

        :param todo_id:
        :return:
        """
        abort_if_todo_doesnt_exist(id)
        service.DepartmentService.delete_department(id)
        return 'Deleted successfully', 204


api.add_resource(DepartmentApi, "/api/v1/departments", "/api/v1/departments/", "/api/v1/departments/<int:id>")
