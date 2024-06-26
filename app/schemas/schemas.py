from app.app import ma

class EventSchema(ma.Schema):
  class Meta:
    fields = (
      'id',
      'eventName',
      'eventStart', 
      'eventEnd', 
      'eventLocation', 
      'eventDescription',
      'eventYear',
      'eventMonth',
      'eventDay', 
      'is_executed'
      )

Event_schema = EventSchema()
Events_schema = EventSchema(many=True)