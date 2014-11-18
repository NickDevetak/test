from app import db
from sqlalchemy.dialects.postgresql import UUID


class Result(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True)
    run_id = db.Column(db.String())
    feature = db.Column(db.String())
    scenario = db.Column(db.String())
    run_time = db.Column(db.String())
    status = db.Column(db.String())

    def __init__(self, run_id, feature, scenario, run_time, status):
        self.run_id = run_id
        self.feature = feature
        self.scenario = scenario
        self.run_time = run_time
        self.status = status

    def __repr__(self):
        return '<id {}>'.format(self.id)
