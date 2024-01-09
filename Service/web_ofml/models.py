import json

from .. import db
from datetime import datetime
from sqlalchemy.dialects.mysql import JSON
from sqlalchemy.event import listens_for
Base = db.Model #declarative_base()

# DROP TABLE web_article_item; DROP TABLE web_property_item; DROP TABLE web_session; DROP TABLE web_user;


def _format_datetime(date: datetime):
    return {
        "year": date.year,
        "month": date.month,
        "day": date.day,
        "hour": date.hour,
        "minute": date.minute,
        "second": date.second,
    }


class ArticleItem(Base):

    __tablename__ = 'web_article_item'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow)
    edit_date = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    article_nr = db.Column(db.String(255), nullable=False)
    program = db.Column(db.String(255), nullable=False)
    session_id = db.Column(db.Integer, db.ForeignKey('web_session.id', ondelete="CASCADE"), nullable=False)
    json = db.Column(JSON, nullable=False)

    @staticmethod
    def delete_by_id(id_: int):
        ArticleItem.query.filter(
            ArticleItem.id == id_
        ).delete()
        db.session.commit()

    @staticmethod
    def get_by_article_program_session_id(article_nr, program, session_id):
        return ArticleItem.query.filter(
            ArticleItem.article_nr == article_nr,
            ArticleItem.program == program,
            ArticleItem.session_id == session_id
        ).first()

    @staticmethod
    def delete_by_article_program_session_id(article_nr, program, session_id):
        ArticleItem.query.filter(
            ArticleItem.article_nr == article_nr,
            ArticleItem.program == program,
            ArticleItem.session_id == session_id
        ).delete()

        db.session.commit()

    @staticmethod
    def update(item: 'ArticleItem', **kwargs):
        item.json = kwargs["json"]
        db.session.commit()
        return item.id

    @staticmethod
    def create(item: 'ArticleItem'):
        db.session.add(item)
        db.session.commit()
        return item.id

    @staticmethod
    def by_session_id(session_id):
        return ArticleItem.query.filter(
            ArticleItem.session_id == session_id
        ).all()

    def as_dict(self):
        return {
            "id": self.id,
            "creationDate": _format_datetime(self.creation_date),
            "editDate": _format_datetime(self.edit_date),
            "program": self.program,
            "articleNr": self.article_nr,
            "sessionId": self.session_id,
            "json": json.loads(self.json)
        }

    @staticmethod
    def all():
        return db.session.query(ArticleItem).all()


class PropertyItem(Base):

    __tablename__ = 'web_property_item'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow)
    edit_date = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    p_class = db.Column(db.String(255), nullable=False)
    program = db.Column(db.String(255), nullable=False)
    json = db.Column(JSON, nullable=False)
    session_id = db.Column(db.Integer, db.ForeignKey('web_session.id', ondelete="CASCADE"), nullable=False)

    @staticmethod
    def delete_by_p_class_program(p_class, program):
        PropertyItem.query.filter(
            PropertyItem.p_class == p_class,
            PropertyItem.program == program
        ).delete()
        db.session.commit()

    @staticmethod
    def create(item: 'PropertyItem'):
        db.session.add(item)
        db.session.commit()
        return item.id

    @staticmethod
    def by_session_id(session_id):
        return PropertyItem.query.filter(
            PropertyItem.session_id == session_id
        ).all()

    def as_dict(self):
        return {
            "id": self.id,
            "creationDate": _format_datetime(self.creation_date),
            "editDate": _format_datetime(self.edit_date),
            "p_class": self.p_class,
            "program": self.program,
            "sessionId": self.session_id,
            "json": json.loads(self.json)
        }


class Session(Base):

    __tablename__ = 'web_session'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    creation_date = db.Column(db.DateTime, default=datetime.now)
    edit_date = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    is_public = db.Column(db.Boolean(), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('web_user.id'), nullable=False)
    article_input = db.Column(db.Text)
    programs_status = db.Column(JSON)
    article_items = db.relationship('ArticleItem', cascade="all, delete", passive_deletes=True)
    property_items = db.relationship('PropertyItem', cascade="all, delete", passive_deletes=True)

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "creationDate": _format_datetime(self.creation_date),
            "editDate": _format_datetime(self.edit_date),
            "isPublic": self.is_public,
            "ownerId": self.owner_id,
            "articleInput": self.article_input,
            "programsStatus": self.programs_status
        }

    @staticmethod
    def by_id(id_):
        return db.session.query(Session).filter(Session.id == id_).first()

    @staticmethod
    def by_email(email):
        user = db.session.query(User).filter(User.email == email).first()
        if user:
            return db.session.query(Session).filter(Session.owner_id == user.id).order_by(Session.edit_date.desc()).all()
        return []

    @staticmethod
    def create(session: 'Session'):
        db.session.add(session)
        db.session.commit()
        return session.id

    @staticmethod
    def update(session: 'Session', **kwargs):
        if "isPublic" in kwargs:
            session.is_public = kwargs["isPublic"]
        if "articleInput" in kwargs:
            session.article_input = kwargs["articleInput"]
        if "name" in kwargs:
            session.name = kwargs["name"]
        db.session.commit()
        return session.id

    @staticmethod
    def delete_by_id(id_: int):
        Session.query.filter(
            Session.id == id_
        ).delete()
        db.session.commit()

    @staticmethod
    def all():
        return db.session.query(Session).all()

    @staticmethod
    def all_with_user():
        return (db.session.query(Session, User)
                .join(User, User.id == Session.owner_id)
                .order_by(Session.edit_date.desc())
                .all())


class User(Base):

    __tablename__ = 'web_user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True)
    name = db.Column(db.Text, nullable=True)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow)
    edit_date = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    sessions = db.relationship('Session')

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


@listens_for(ArticleItem.json, "set", named=True)
def on_article_set(**kwargs):
    target: ArticleItem = kwargs["target"]
    session: Session = Session.by_id(target.session_id)
    session.edit_date = datetime.now()
    db.session.commit()


@listens_for(PropertyItem.json, "set", named=True)
def on_article_set(**kwargs):
    target: PropertyItem = kwargs["target"]
    session: Session = Session.by_id(target.session_id)
    session.edit_date = datetime.now()
    db.session.commit()
