from app.app import ma

class TodoSchema(ma.Schema):
  class Meta:
    fields = ('id', 'name', 'is_executed')

todo_schema = TodoSchema()
todos_schema = TodoSchema(many=True)