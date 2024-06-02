from app.app import db

class Event(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  eventName = db.Column(db.String(100))
  eventStart = db.Column(db.String(100))
  eventEnd = db.Column(db.String(100)) #ajt des toris col regarder structure int
  eventLocation = db.Column(db.String(100))
  eventDescription = db.Column(db.String(100))
  eventYear = db.Column(db.Integer)
  eventMonth = db.Column(db.Integer)
  eventDay = db.Column(db.Integer)
  is_executed = db.Column(db.Boolean)

  def __init__(self, eventName, eventStart, eventEnd, eventLocation, eventDescription, eventYear, eventMonth, eventDay, is_executed):#ajt trois col
    self.eventName = eventName
    self.eventStart = eventStart
    self.eventEnd = eventEnd
    self.eventLocation = eventLocation
    self.eventDescription = eventDescription
    self.eventYear = eventYear
    self.eventMonth = eventMonth
    self.eventDay = eventDay
    self.is_executed = is_executed
