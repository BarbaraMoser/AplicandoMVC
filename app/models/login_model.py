from datetime import datetime

from database import db


class Login(db.Model):
    __tablename__ = 'logins'

    id = db.Column(db.String(36), primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    logged_in = db.Column(db.DateTime, default=lambda: datetime.now())

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
        }
