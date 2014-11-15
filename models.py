from app import db
from sqlalchemy.dialects.postgresql import JSON


class Result(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True)
    feature = db.Column(db.String())
    run_time = db.Column(db.String())

    def __init__(self, feature, run_time):
        self.feature = feature
        self.run_time = run_time

    def __repr__(self):
        return '<id {}>'.format(self.id)
