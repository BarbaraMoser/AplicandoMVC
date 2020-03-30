from datetime import datetime
from xmlrpc.client import DateTime

from database import db


class Login(db.Model):
    __tablename__ = 'logins'

    id = db.Column(db.String(36), primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    # logged_in = db.Column(DateTime, default=lambda: datetime.now(), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
        }
