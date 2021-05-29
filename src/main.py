from flask import Flask, app
from flask import jsonify
import json

from flask.globals import request
from flask.json import JSONEncoder
# app = Flask(__name__)
# @app.route('/')
# def hello_world():
#     return 'Olá'


app = Flask(__name__)
app.run(debug=True)

with open('tasks.json', 'r') as myfile:
    data=myfile.read()
obj = json.loads(data)
@app.route('/getall', methods=['GET'])
def getTasks():
    return jsonify(obj)

@app.route('/create', methods=['POST'])
def createTask():
    req_data = request.get_json()
    obj.append(req_data)
    return jsonify(req_data)

@app.route('/delete', methods=['DELETE'])
def deleteTask():
    req_data = request.get_json()
    for id, task in enumerate(obj):
        if task.get('task') == req_data["task"]:
            obj.pop(id)
            return jsonify(req_data)
    return 'Não encontrado'

@app.route('/update', methods=['PUT'])
def updateTask():
    req_data = request.get_json()
    for id, task in enumerate(obj):
        if task.get('task') == req_data['task']:
            obj.pop(id)
            obj.insert(id, req_data)
            break
    return jsonify(req_data)


