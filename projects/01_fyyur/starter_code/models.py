import flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy

Show = db.Table('shows',
               db.Column('artist_id', db.Integer, db.ForeignKey('artist.id'), primary_key=True),
               db.Column('venue_id', db.Integer, db.ForeignKey('venue.id'), primary_key=True),
               db.Column('start_time', db.DateTime(timezone=True), primary_key=True))
#def __init__(shows, artist_id, venue_id, start_time):
  #shows.artist_id = artist_id
  #shows.venue_id = venue_id
  #shows.start_time = start_time

class Artist(db.Model):
    __tablename__ = 'artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    city = db.Column(db.String(120), nullable=True)
    state = db.Column(db.String(120), nullable=True)
    phone = db.Column(db.String(120), nullable=True)
    image_link = db.Column(db.String(500), nullable=True)
    facebook_link = db.Column(db.String(120), nullable=True)
    website = db.Column(db.String(120), nullable=True)
    seeking_venue = db.Column(db.Boolean, nullable=True)
    seeking_description = db.Column(db.String(500), nullable=True)
    genres = db.Column(db.ARRAY(db.String(120)), nullable=True)
    playing_at = db.relationship('Venue', secondary=Show, backref=db.backref('hosts', lazy='joined'))
    start_time = db.Column(db.DateTime(timezone=True), nullable=True)

    def __init__(self, name, city, state, phone, image_link, facebook_link, website, seeking_talent, seeking_description, genres):
      self.name = name
      self.city = city
      self.state = state
      self.phone = phone
      self.image_link = image_link
      self.facebook_link = facebook_link
      self.website = website
      self.seeking_talent = seeking_talent
      self.seeking_description = seeking_description
      self.genres = genres

class Venue(db.Model):
    __tablename__ = 'venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=True)
    city = db.Column(db.String(120), nullable=True)
    state = db.Column(db.String(120), nullable=True)
    address = db.Column(db.String(120), nullable=True)
    phone = db.Column(db.String(120), nullable=True)
    image_link = db.Column(db.String(500), nullable=True)
    facebook_link = db.Column(db.String(120), nullable=True)
    website = db.Column(db.String(120), nullable=True)
    seeking_talent = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.String(500), nullable=True) 
    genres = db.Column(db.ARRAY(db.String(120)), nullable=True) 
    start_time = db.Column(db.DateTime(timezone=True), nullable=True)

    def __init__(self, name, city, state, address, phone, image_link, facebook_link, website, seeking_talent, seeking_description, genres):
      self.name = name
      self.city = city
      self.state = state
      self.address = address
      self.phone = phone
      self.image_link = image_link
      self.facebook_link = facebook_link
      self.website = website
      self.seeking_talent = seeking_talent
      self.seeking_description = seeking_description
      self.genres = genres
    