from app import db


class Result(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True)
    feature = db.Column(db.String())
    scenario = db.Column(db.String())
    run_time = db.Column(db.String())
    status = db.Column(db.String())

    def __init__(self, feature, scenario, run_time, status):
        self.feature = feature
        self.scenario = scenario
        self.run_time = run_time
        self.status = status

    def __repr__(self):
        return '<id {}>'.format(self.id)
