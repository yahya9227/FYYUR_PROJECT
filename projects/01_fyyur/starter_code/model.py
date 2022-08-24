
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class  Show(db.Model):
    __tablename__ = 'Show'
    id = db.Column(db. Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'), primary_key=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id'), primary_key=False)
    start_time = db.Column(db.DateTime(timezone=True))

class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    website_link = db.Column(db.String(120))
    facebook_link = db.Column(db.String(120))
    seeking_talent = db.Column(db.String(120))
    seeking_description = db.Column(db.String(120))
    shows = db.relationship('Show', backref=db.backref('Venue'), lazy='dynamic')

    # TODO: implement any missing fields, as a database migration using Flask-Migrate
    def __repr__(self):

          return f'<Venue ID: {self.id} name: {self.name}, city: {self.city}>'

class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website_link = db.Column(db.String(120))
    seeking_venue = db.Column(db.String(120))
    seeking_description = db.Column(db.String(120))
    shows = db.relationship('Show', backref=db.backref('Artist'), lazy='dynamic')


    def __repr__(self):

          return f'<Artist ID: {self.id} name: {self.name}, city: {self.city}>'