from flask import request, jsonify
from flask import current_app as app

from app.app import db

from app.models.Event_model import Event as EventItem
from app.schemas.schemas import Event_schema, Events_schema

class EventController:
  @app.route('/event', methods=['GET'])
  def get_events():
    all_events = EventItem.query.all()
    result = Events_schema.dump(all_events)
    return jsonify(result)

  @app.route('/event/<id>', methods=['GET'])
  def get_event_by_id(id):
    event = EventItem.query.get(id)
    if not event: return jsonify({"error": "La tâche n'existe pas"}), 404
    return Event_schema.jsonify(event)
  
  @app.route('/event', methods=['POST'])
  def create_event():
    #name = request.json['name']
    eventName = request.json['eventName']
    eventStart = request.json['eventStart']
    eventEnd = request.json['eventEnd']
    eventLocation = request.json['eventLocation']
    eventDescription = request.json['eventDescription']
    is_executed = request.json['is_executed']

    # verifier si le nom de la tâche est vide
    if not eventName: return jsonify({"error": "Le nom de la tâche est obligatoire"}), 400
    
    # verifier si le nom de la tâche est déjà utilisé
    event = EventItem.query.filter_by(eventName=eventName).first()
    if event: return jsonify({"error": "Cette tâche existe déjà"}), 400
    #new_event_item = EventItem(name, is_executed)
    new_event_item = EventItem(  
                               eventName, 
                               eventStart, 
                               eventEnd, 
                               eventLocation, 
                               eventDescription,
                               is_executed
                               )
    db.session.add(new_event_item)
    db.session.commit()

    return Event_schema.jsonify(new_event_item)
  
  @app.route('/event/<id>', methods=['PUT', 'PATCH'])
  def update_event(id):
    event = EventItem.query.get(id)
    
    #if request.json['name']: name = request.json['name']
    if request.json['eventName']: eventName = request.json['eventName']
    if request.json['eventStart']: eventStart = request.json['eventStart']
    if request.json['eventEnd']: eventEnd = request.json['eventEnd']
    if request.json['eventLocation']: eventLocation = request.json['eventLocation']
    if request.json['eventDescription']: eventDescription = request.json['eventDescription']
    if request.json['is_executed']: is_executed = request.json['is_executed']
    pass

  @app.route('/event/<id>', methods=['PUT', 'PATCH'])
  def execute_event(id):
    event = EventItem.query.get(id)
    if not event: return jsonify({"error": "La tâche n'existe pas"}), 404
    event.is_executed = not event.is_executed
    db.session.commit()
    return Event_schema.jsonify(event)

  @app.route('/event/<id>', methods=['DELETE'])
  def delete_event(id):
    event_to_delete = EventItem.query.get(id)
    if not event_to_delete: return jsonify({"error": "La tâche n'existe pas"}), 404
    db.session.delete(event_to_delete)
    db.session.commit()
    # retourner un message de succès
    return jsonify({"success": "La tâche a été supprimée"})
