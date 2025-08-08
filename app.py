# create a virtual env -> py -m venv myvenv
# myvenv\scripts\activate
# permission error: Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
# app.py
# requirements.txt file -> flask not a command
# pip install -r requirements.txt


from flask import Flask
from flask import request, Response
import uuid
from flask_cors import CORS

from utils import createTask, viewAllTask

app = Flask(__name__)

CORS(app, resources={r'/*': { "origins": "*"}}, supports_credentials=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    return { 'message': 'hello'}


@app.route('/create-task', methods=['POST'])
def create_task():
    if request.method == 'POST':
        task = request.get_json()
        tasks = createTask({ 'name': task.get('task_name'), 'id': str(uuid.uuid4())})
        return { 'data': tasks }
    

@app.route('/view-all-data', methods=['GET'])
def getAllTasks():
    return viewAllTask()

if __name__ == '__main__':
    app.run('localhost', 4000, debug=True)