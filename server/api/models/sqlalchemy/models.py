""" Database models file.
Insert all tables, models, and schemas for the Database here."""
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import Column, Integer, String, Float

db = SQLAlchemy()
ma = Marshmallow()


class QuestionResponse(db.Model):
    questionId = db.Column(db.Integer, primary_key=True)
    responseValue = db.Column(db.String(100))
    candidateId = db.Column(db.Integer)

    def __init__(self, responseValue, candidateId):
        self.responseValue = responseValue
        self.candidateId = candidateId


class ResponseSchema(ma.Schema):
    class Meta:
        fields = ('questionId', 'responseValue', 'candidateId')


class Candidate(db.Model):
    candidateId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def __init__(self, name):
        self.name = name


class CandidateSchema(ma.Schema):
    class Meta:
        fields = ('candidateId', 'name')


class Question(db.Model):
    questionId = db.Column(db.Integer, primary_key=True)
    questionText = db.Column(db.String(100))

    def __init__(self, questionText):
        self.questionText = questionText


class QuestionSchema(ma.Schema):
    class Meta:
        fields = ('formId', 'questionText', 'questionId')


class Form(db.Model):
    form_id = db.Column(db.Integer, primary_key=True)
    form_name = db.Column(db.String(100))
    form_description = db.Column(db.String(100))

    def __init__(self, form_name, form_description):
        self.form_name = form_name
        self.form_description = form_description


class FormSchema(ma.Schema):
    class Meta:
        fields = ('formId', 'formName', 'formDescription')


class FormQuestion(db.Model):
    form_id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, primary_key=True)

    def __init__(self, form_id, question_id):
        self.form_id = form_id
        self.question_id = question_id


class FormQuestionSchema(ma.Schema):
    class Meta:
        fields = ('formId', 'questionId')


class HousingLocation(db.Model):
    __tablename__ = 'locations'
    locationId = db.Column(db.Integer, primary_key=True)
    location_id = Column(Integer, primary_key=True)
    latitude = Column(Float)
    longitude = Column(Float)
    housing_type_id = Column(Integer)
    beds_available = Column(Integer)
    name = db.Column(db.String(100))

    def __init__(self, name):
        self.name = name


class LocationSchema(ma.Schema):
    class Meta:
        fields = ('location_id', 'name', 'latitude', 'longitude', 'housing_type_id', 'beds_available')
