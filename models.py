from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Employee(db.Model):

    __tablename__ = 'employees' 

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    username = db.Column(db.String)
    password = db.column(db.Varchar)
    skills = db.Column(db.String)
    experience = db.Column(db.Integer)

    def __init__(self, name, email, skills, experience):
        self.name = name
        self.email = email
        self.skills = skills
        self.experience = experience

    def __repr__(self):
        return f'<Employee {self.id} {self.name} {self.email} {self.skills} {self.experience}>'
    


class Employer(db.Model):
   
    __tablename__ = 'employers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    username = db.Column(db.String)
    password = db.column(db.Varchar)
    description = db.Column(db.Text)

    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __repr__(self):
        return f'<Employer {self.id} {self.name} {self.description}>'



class Job(db.Model):
   
    __tablename__ = 'jobs'

    id = db.Column(db.Integer, primary_key=True) 
    title = db.Column(db.String)
    description = db.Column(db.Text)
    salary = db.Column(db.Integer)
    location = db.Column(db.String)
    type = db.Column(db.String)

    def __init__(self, title, description, location, type):
        self.title = title
        self.description = description
        self.location = location
        self.type = type

    def __repr__(self):
        return f'<Job {self.id} {self.title}>'

class Rating(db.Model):
    
    __tablename__ = 'ratings'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)
    date = db.Column(db.DateTime)

    def __init__(self, rating, date):
        self.rating = rating
        self.date = date

    def __repr__(self):
        return f'<Rating {self.id} {self.rating}>'