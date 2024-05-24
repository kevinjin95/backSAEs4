from flask import request, jsonify
from flask import current_app as app

from app.app import db

from app.models.Task_model import TodoItem
from app.schemas.schemas import todo_schema, todos_schema

class TaskController:
  @app.route('/todo', methods=['GET'])
  def get_todos():
    all_todos = TodoItem.query.all()
    result = todos_schema.dump(all_todos)
    return jsonify(result)

  @app.route('/todo/<id>', methods=['GET'])
  def get_todo_by_id(id):
    todo = TodoItem.query.get(id)
    if not todo: return jsonify({"error": "La tâche n'existe pas"}), 404
    return todo_schema.jsonify(todo)
  
  @app.route('/todo', methods=['POST'])
  def create_todo():
    name = request.json['name']
    is_executed = request.json['is_executed']

    # verifier si le nom de la tâche est vide
    if not name: return jsonify({"error": "Le nom de la tâche est obligatoire"}), 400
    
    # verifier si le nom de la tâche est déjà utilisé
    todo = TodoItem.query.filter_by(name=name).first()
    if todo: return jsonify({"error": "Cette tâche existe déjà"}), 400
    
    new_todo_item = TodoItem(name, is_executed)
    db.session.add(new_todo_item)
    db.session.commit()

    return todo_schema.jsonify(new_todo_item)
  
  @app.route('/todo/<id>', methods=['PUT', 'PATCH'])
  def update_todo(id):
    todo = TodoItem.query.get(id)
    
    if request.json['name']: name = request.json['name']
    if request.json['is_executed']: is_executed = request.json['is_executed']
    
    pass

  @app.route('/todo/<id>', methods=['PUT', 'PATCH'])
  def execute_todo(id):
    todo = TodoItem.query.get(id)
    if not todo: return jsonify({"error": "La tâche n'existe pas"}), 404
    todo.is_executed = not todo.is_executed
    db.session.commit()
    return todo_schema.jsonify(todo)

  @app.route('/todo/<id>', methods=['DELETE'])
  def delete_todo(id):
    todo_to_delete = TodoItem.query.get(id)
    if not todo_to_delete: return jsonify({"error": "La tâche n'existe pas"}), 404
    db.session.delete(todo_to_delete)
    db.session.commit()
    # retourner un message de succès
    return jsonify({"success": "La tâche a été supprimée"})
