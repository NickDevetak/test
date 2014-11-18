from flask import Flask, request, make_response, render_template
from flask.ext.sqlalchemy import SQLAlchemy
import os
import json
import uuid

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

@app.route('/results', methods=['GET'])
def results():
    #all_results = Result.query.all()
    all_results = Result.query.filter_by(feature = 'feature1')
    return render_template('results.html', results=all_results)

@app.route('/upload', methods=['POST'])
def upload_results():
    json_text = request.get_json()
    run_id = uuid.uuid4()
    for i in json_text['results']:
        result = Result(
            feature=i['feature'],
            scenario=i['scenario'],
            run_time=i['run_time'],
            status=i['status'],
            )
        db.session.add(result)
        db.session.commit()
    return make_response(
            json.dumps({
                'message': 'OK',
                'status_code': 201
            }),
            201)

if __name__ == '__main__':
    app.run()
