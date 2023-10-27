from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Employee(db.Model):

    __tablename__ = 'employees' 

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    skills = db.Column(db.String)
    experience = db.Column(db.Integer)

    def __init__(self, name, email, skills, experience):
        self.name = name
        self.email = email
        self.skills = skills
        self.experience = experience
        

class Job(db.Model):
   
    __tablename__ = 'jobs'

    id = db.Column(db.Integer, primary_key=True) 
    title = db.Column(db.String)
    description = db.Column(db.Text)
    location = db.Column(db.String)
    type = db.Column(db.String)

    def __init__(self, title, description, location, type):
        self.title = title
        self.description = description
        self.location = location
        self.type = type
