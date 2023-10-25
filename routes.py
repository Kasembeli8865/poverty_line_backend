from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import db, Employees, Employers, Jobs, Ratings

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)



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
        db.session.commit()

        response_dict = new_employee.to_dict()

        response = make_response(
            jsonify(response_dict),
            201,
        )

        return response
   
api.add_resource(Employees, '/employees')   

class EmployeesByID(Resource):
     
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
api.add_resource(EmployeesByID, '/employees/<int:id>')  


################### EMPLOYERS ################
class Employers(Resource):
    def get(self):
        response_dict_list = [n.to_dict() for n in Employer.query.all()]

        response = make_response(
            jsonify(response_dict_list),
            200,
        )

        return response
    
    def post(self):
        new_employer = Employer(
            name=request.json['name'],
            description=request['description']
        )

        db.session.add(new_employer)
        db.session.commit()

        response_dict = new_employer.to_dict()

        response = make_response(
            jsonify(response_dict),
            201,
        )

        return response
   
api.add_resource(Employers, '/employers')   

class EmployersByID(Resource):
     
    def patch(self,id):
        employer = Employer.query.get(int(id))
        for attr in request.json:
            setattr(employer, attr, request.json[attr])
        db.session.add(employer)
        db.session.commit()

        response_dict = employer.to_dict()

        response = make_response(
            jsonify(response_dict),
            200,
        )
        return response
api.add_resource(EmployersByID, '/employers/<int:id>')  


################### JOBS ################
class Jobs(Resource):
    def get(self):
        response_dict_list = [n.to_dict() for n in Job.query.all()]

        response = make_response(
            jsonify(response_dict_list),
            200,
        )

        return response
    
    def post(self):
        new_job = Job(
            title=request.json['title'],
            description=request['description'],
            location=request['location'],
            type=request['type']
        )

        db.session.add(new_job)
        db.session.commit()

        response_dict = new_job.to_dict()

        response = make_response(
            jsonify(response_dict),
            201,
        )

        return response
   
api.add_resource(Jobs, '/jobs')   

class JobByID(Resource):
    def get(self, id):
        response_dict = Job.query.get(int(id))
        response = make_response(
            jsonify(response_dict),
            200,
        )
        return response

    def patch(self,id):
        job = Job.query.get(int(id))
        for attr in request.json:
            setattr(job, attr, request.json[attr])
        db.session.add(job)
        db.session.commit()

        response_dict = job.to_dict()

        response = make_response(
            jsonify(response_dict),
            200,
        )
        return response
    
    def delete(self, id):
        job = Job.query.get(int(id))
        db.session.delete(job)
        db.session.commit()

        response_dict = {
            'message':'job succesfully deleted'
        }

        reponse = make_response(
            jsonify(response_dict),
            200,
        )

        return reponse
api.add_resource(JobByID, '/jobs/<int:id>')  


################### RATINGS ################
class Ratings(Resource):
    def get(self):
        response_dict_list = [n.to_dict() for n in Rating.query.all()]

        response = make_response(
            jsonify(response_dict_list),
            200,
        )

        return response
    
    def post(self):
        new_rating = Rating(
            rating=request.json['rating'],
            date=request.json['date']
        )

        db.session.add(new_rating)
        db.session.commit()

        response_dict = new_rating.to_dict()

        response = make_response(
            jsonify(response_dict),
            201,
        )

        return response
   
api.add_resource(Ratings, '/ratings')   

class RatingByID(Resource):
    def get(self, id):
        response_dict = Rating.query.get(int(id))
        response = make_response(
            jsonify(response_dict),
            200,
        )
        return response

    def patch(self,id):
        rating = Rating.query.get(int(id))
        for attr in request.json:
            setattr(rating, attr, request.json[attr])
        db.session.add(rating)
        db.session.commit()

        response_dict = rating.to_dict()

        response = make_response(
            jsonify(response_dict),
            200,
        )
        return response
    
    def delete(self, id):
        rating = Rating.query.get(int(id))
        db.session.delete(rating)
        db.session.commit()

        response_dict = {
            'message':'rating succesfully deleted'
        }

        reponse = make_response(
            jsonify(response_dict),
            200,
        )

        return reponse
api.add_resource(RatingByID, '/ratings/<int:id>')  
