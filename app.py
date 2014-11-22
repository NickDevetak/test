from flask import Flask, request, make_response, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import func
from sqlalchemy.sql import label
from sqlalchemy import desc

import os
import json
import uuid
import datetime
import hashlib

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)
from models import *

@app.route('/')
def hello():
    run_id = uuid.uuid4()
    return "Hello World! %s" % run_id

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

@app.route('/results')
def results():
    all_results = db.session.query(Result.run_id, Result.run_date, label('count', func.count(Result.id))).group_by(Result.run_id, Result.run_date).order_by(desc(Result.run_date)).all()
    print all_results
    return render_template('results.html', results=all_results)

@app.route('/upload', methods=['POST'])
def upload_results():
    json_text = request.get_json()
    run_id_value = str(uuid.uuid4())
    run_date_value = datetime.datetime.now()
    for i in json_text['results']:
        print i['steps'][1]
        result = Result(
            run_id=run_id_value,
            feature=i['feature'],
            scenario=i['scenario'],
            run_time=i['run_time'],
            status=i['status'],
            run_date=run_date_value,
            scenario_check_sum=hashlib.md5(i['scenario_steps']).hexdigest(),
            )
        db.session.add(result)
    db.session.commit()
    return make_response(
            json.dumps({
                'message': 'OK',
                'status_code': 201
            }),
            201)

@app.route('/run-results/<run_id>')
def run_results(run_id):
    run_results = db.session.query(Result.feature, Result.scenario, Result.status, Result.run_time, Result.scenario_check_sum).filter_by(run_id = run_id).all()
    return render_template('run_results.html', run_id=run_id, results=run_results)

@app.route('/scenario/<scenario_check_sum>')
def scenario(scenario_check_sum):
    scenario_list = db.session.query(Result.scenario, Result.status, Result.run_date, Result.run_time).filter_by(scenario_check_sum = scenario_check_sum).order_by(desc(Result.run_date)).all()
    return render_template('scenario_history.html', results=scenario_list)

if __name__ == '__main__':
    app.run()
