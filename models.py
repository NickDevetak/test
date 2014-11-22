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
    run_date = db.Column(db.DateTime)
    scenario_check_sum = db.Column(db.String())
    scenario_steps = db.Column(db.String())

    def __init__(self, run_id, feature, scenario, run_time, status, run_date, scenario_check_sum, scenario_steps):
        self.run_id = run_id
        self.feature = feature
        self.scenario = scenario
        self.run_time = run_time
        self.status = status
        self.run_date = run_date
        self.scenario_check_sum = scenario_check_sum
        self.scenario_steps = scenario_steps


    def __repr__(self):
        return '<feature {0.feature} scenario {0.scenario}>'.format(self.feature, self.scenario)
