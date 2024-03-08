from Service import db
from datetime import datetime
from sqlalchemy.dialects.mysql import JSON
from sqlalchemy.event import listens_for
from Service.tables import Base


def _format_datetime(date: datetime):
    return {
        "year": date.year,
        "month": date.month,
        "day": date.day,
        "hour": date.hour,
        "minute": date.minute,
        "second": date.second,
    }


class User(Base):

    __tablename__ = 'web_user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True)
    name = db.Column(db.Text, nullable=True)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow)
    edit_date = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def as_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            "creationDate": _format_datetime(self.creation_date),
            "editDate": _format_datetime(self.edit_date),
        }

    @staticmethod
    def by_email(email):
        return db.session.query(User).filter(User.email == email).first()

    @staticmethod
    def create(user: 'User'):
        db.session.add(user)
        db.session.commit()
        return user.id

    @staticmethod
    def all():
        return db.session.query(User).all()

