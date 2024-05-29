from app.app import db

class Event(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  eventName = db.Column(db.String(100))
  eventStart = db.Column(db.String(100))
  eventEnd = db.Column(db.String(100))
  eventLocation = db.Column(db.String(100))
  eventDescription = db.Column(db.String(100))
  is_executed = db.Column(db.Boolean)

  def __init__(self, eventName, eventStart, eventEnd, eventLocation, eventDescription, is_executed):
    self.is_executed = is_executed
    self.eventName = eventName
    self.eventStart = eventStart
    self.eventEnd = eventEnd
    self.eventLocation = eventLocation
    self.eventDescription = eventDescription
