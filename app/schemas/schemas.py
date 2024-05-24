from app.app import ma

class EventSchema(ma.Schema):
  class Meta:
    fields = ('id', 'name', 'is_executed')

Event_schema = EventSchema()
Events_schema = EventSchema(many=True)