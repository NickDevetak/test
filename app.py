from flask import Flask, request
from flask.ext.sqlalchemy import SQLAlchemy
import os
import json

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)
from models import *

@app.route('/')
def hello():
    result = Result(
        feature="feature1",
        run_time="0.1",
        )
    db.session.add(result)
    db.session.commit()
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

@app.route('/upload', methods=['POST'])
def upload_results():

    json_text = request.get_json()
    print json_text

    json_object = request.data
    print json_object

    for i in json_text['results']:
        print i['feature']
        print i['run_time']
        result = Result(
            feature=i['feature'],
            run_time=i['run_time'],
            )
        db.session.add(result)
        db.session.commit()

    return "Success"

if __name__ == '__main__':
    app.run()
