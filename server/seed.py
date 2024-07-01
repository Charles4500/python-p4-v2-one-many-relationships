#!/usr/bin/env python3
# server/seed.py

import datetime
from app import app
from models import db, Employee, Review, Onboarding

with app.app_context():
    # Delete all rows in tables
    Employee.query.delete()
    Review.query.delete()
    Onboarding.query.delete()

    # Add model instances to database
    uri = Employee(name="Uri Lee", hire_date=datetime.datetime(2024, 5, 17))
    tristan = Employee(name="Tristan Tal",
                       hire_date=datetime.datetime(2024, 1, 30))
    db.session.add_all([uri, tristan])
    db.session.commit()

    # 1..many relationship between Employee and Review
    uri_2024 = Review(year=2024,
                      summary="Great web developer!",
                      employee_id=uri)
    tristan_2024 = Review(year=2024,
                          summary="Good coding skills, often late to work",
                          employee_id=tristan)
    tristan_2024 = Review(year=2024,
                          summary="Strong coding skills, takes long lunches",
                          employee_id=tristan)
    tristan_2024 = Review(year=2024,
                          summary="Awesome coding skills, dedicated worker",
                          employee_id=tristan)
    db.session.add_all([uri_2024, tristan_2024, tristan_2024, tristan_2024])
    db.session.commit()

    # 1..1 relationship between Employee and Onboarding
    uri_onboarding = Onboarding(orientation=datetime.datetime(2024, 3, 27))
    tristan_onboarding = Onboarding(
        orientation=datetime.datetime(2024, 1, 20, 14, 30), forms_complete=True
    )
    db.session.add_all([uri_onboarding, tristan_onboarding])
    db.session.commit()
