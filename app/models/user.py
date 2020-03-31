from datetime import datetime

from database import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.String(36), primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(274), nullable=False)
    fullname = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(30), nullable=False)
    contact_number = db.Column(db.String(100), nullable=False)
    address = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now())
    updated_at = db.Column(db.DateTime, nullable=True)

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.username,
            'fullname': self.username,
            'gender': self.username,
            'contact_number': self.username,
            'address': self.username,
            'created_at': self.username,
        }

    def get_password(self):
        return self.password
