from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


################### EMPLOYEES ################
class Employees(Resource):
    def get(self):
        response_dict_list = [n.to_dict() for n in Employee.query.all()]

        response = make_response(
            jsonify(response_dict_list),
            200,
        )

        return response
    
    def post(self):
        new_employee = Employee(
            name=request.json['name'],
            email=request.json['email'],
            skills=request.json['skills'],
            experience=request.json['experience']
        )

        db.session.add(new_employee)
        db,session.commit()

        response_dict = new_employee.to_dict()

        response = make_response(
            jsonify(response_dict),
            201,
        )

        return response
   
api.add_resource(Employees, '/employees')   

class EditEmployees(Resource):
     
    def patch(self,id):
        employee = Employee.query.get(int(id))
        for attr in request.json:
            setattr(employee, attr, request.json[attr])
        db.session.add(employee)
        db.session.commit()

        response_dict = employee.to_dict()

        response = make_response(
            jsonify(response_dict),
            200,
        )
        return response
api.add_resource(EditEmployees, '/employees/edit')  
