from app import db
from models import Task
from datetime import datetime

db.create_all()
t = Task(title="abc", date=datetime.utcnow())
db.session.add(t)

t = Task(title="xyz", date=datetime.utcnow())
db.session.add(t)

db.session.commit()
print(Task.query.all())