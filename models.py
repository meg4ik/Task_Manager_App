from app import db
from datetime import datetime

class Writing(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    content = db.Column(db.String(200), nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)
