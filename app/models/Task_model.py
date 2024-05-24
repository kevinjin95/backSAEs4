from app.app import db

class TodoItem(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  is_executed = db.Column(db.Boolean)

  def __init__(self, name, is_executed):
    self.name = name
    self.is_executed = is_executed