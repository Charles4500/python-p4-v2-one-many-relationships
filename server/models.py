# server/models.py
# Model/Modelling --> Is basically to mould or make something
# Models are basically classes in python --> And this classes are what will then turn to be tables in our database
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData(
    naming_convention={
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    }
)

db = SQLAlchemy(metadata=metadata)


class Employee(db.Model):
    # This is  a constant variable or this will basically be the name of our table
    __tablename__ = "employees"

    # This will be columns in our database and columns are just basically variables or containers to hold our data
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    hire_date = db.Column(db.Date)

    # Relationship mapping the employee to related reviews
    reviews = db.relationship(
        'Review', back_populates='employee', cascade='all,delete-orphan')

    # Relationship mapping employee to related onboarding
    onboarding = db.relationship(
        'Onboarding', back_populates='employee', cascade='all,delete-orphan')

    def __repr__(self):
        return f"<Employee {self.id}, {self.name}, {self.hire_date}>"


class Onboarding(db.Model):
    # This is  a constant variable or this will basically be the name of our table
    __tablename__ = "onboardings"

# This will be columns in our database and columns are just basically variables or containers to hold our data
    id = db.Column(db.Integer, primary_key=True)
    orientation = db.Column(db.DateTime)
    forms_complete = db.Column(db.Boolean, default=False)
    # Foreign key to store the employee id
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))

    # Relationship
    employee = db.relationship('Employee', back_populates='onboarding')

    def __repr__(self):
        return f"<Onboarding {self.id}, {self.orientation}, {self.forms_complete}>"


class Review(db.Model):
    # This is  a constant variable or this will basically be the name of our table
    __tablename__ = "reviews"

# This will be columns in our database and columns are just basically variables or containers to hold our data
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    summary = db.Column(db.String)
    # Foreign key stores the employee id
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))

    # Relationship mapping the review to related employee
    employee = db.relationship('Employee', back_populates='reviews')

    def __repr__(self):
        return f"<Review {self.id}, {self.year}, {self.summary}>"
