from flask import request, jsonify
from flask import current_app as app

from app.app import db

from app.models.Event_model import Event as EventItem
from app.schemas.schemas import Event_schema, Events_schema

class EventController:
  @app.route('/event', methods=['GET'])
  def get_events():
    all_events = EventItem.query.all()#localhost/event liste de tous les listes
    result = Events_schema.dump(all_events)#objet model et les transformer en json grâce à marshmallow
    return jsonify(result)

  @app.route('/event/<id>', methods=['GET'])
  def get_event_by_id(id):
    event = EventItem.query.get(id)
    if not event: return jsonify({"error": "La tâche n'existe pas"}), 404
    return Event_schema.jsonify(event)
  
  @app.route('/event', methods=['POST'])
  def create_event():
    data = request.json
    eventName = data.get('eventName')
    if not eventName: return jsonify({"error": "Le nom de la tâche est obligatoire"}), 400
    
    if EventItem.query.filter_by(eventName=eventName).first(): return jsonify({"error": "Cette tâche existe déjà"}), 400

    new_event_item = EventItem(
      eventName,
      data.get('eventStart'),
      data.get('eventEnd'),
      data.get('eventLocation'),
      data.get('eventDescription'),
      data.get('eventYear'),
      data.get('eventMonth'),
      data.get('eventDay'),
      data.get('is_executed')
    )
    db.session.add(new_event_item)
    db.session.commit()

    return Event_schema.jsonify(new_event_item), 201
  
  @app.route('/event/<id>', methods=['PUT', 'PATCH'])
  def update_event(id):
    event = EventItem.query.get(id)
    if not event: return jsonify({"error": "La tâche n'existe pas"}), 404
    
    data = request.json
    if 'eventName' in data:
      if EventItem.query.filter_by(eventName=data['eventName']).first(): return jsonify({"error": "Cette évenement existe déjà"}), 400
      event.eventName = data['eventName']
    
    event.eventStart = data.get('eventStart', event.eventStart)
    event.eventEnd = data.get('eventEnd', event.eventEnd)
    event.eventLocation = data.get('eventLocation', event.eventLocation)
    event.eventDescription = data.get('eventDescription', event.eventDescription)
    event.eventYear = data.get('eventYear', event.eventYear)
    event.eventMonth = data.get('eventMonth', event.eventMonth)
    event.eventDay = data.get('eventDay', event.eventDay)
    event.is_executed = data.get('is_executed', event.is_executed)
    db.session.commit()
    return jsonify({"success": "La tâche a été modifiée"})

  @app.route('/event/<id>/execute', methods=['PATCH'])
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
    return jsonify({"success": "La tâche a été supprimée"}), 204
