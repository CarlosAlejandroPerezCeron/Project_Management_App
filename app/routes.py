from app import app, db
from app.models import Project
from flask import request, jsonify

@app.route('/')
def index():
    return 'Project Management API'

@app.route('/projects', methods=['GET'])
def get_projects():
    projects = Project.query.all()
    return jsonify([{'name': project.name, 'description': project.description, 'status': project.status} for project in projects])

@app.route('/projects', methods=['POST'])
def add_project():
    data = request.get_json()
    new_project = Project(name=data['name'], description=data['description'], status=data['status'])
    db.session.add(new_project)
    db.session.commit()
    return jsonify({'message': 'Project added'}), 201
