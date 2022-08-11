from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import relationship

db = SQLAlchemy()

planetFavourites = db.Table('planetFavourites',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('planet_id', db.Integer, db.ForeignKey('planet.id'), primary_key=True)
)

peopleFavourites = db.Table('peopleFavourites',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('person_id', db.Integer, db.ForeignKey('person.id'), primary_key=True)
)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(30), nullable=False)
    lastName = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(8), unique=False, nullable=False)
    peopleFavourites = db.relationship("Person", secondary=peopleFavourites, backref="users", lazy=True)
    planetFavourites = db.relationship("Planet", secondary=planetFavourites, backref="users", lazy=True)
    
    def __repr__(self):
        return '<User %r>' % self.firstName

    def serialize(self):
        return {
            "id": self.id,
            "first_name": self.firstName,
            "last_name": self.lastName,
            "email": self.email
            # do not serialize the password, its a security breach
        }

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    height = db.Column(db.String(100), unique=True, nullable=False)
    mass = db.Column(db.String(100),  unique=True, nullable=False)
    hair_color = db.Column(db.String(100),  unique=True, nullable=False)
    skin_color = db.Column(db.String(100),  unique=True, nullable=False)
    eye = db.Column(db.String(100),  unique=True, nullable=False)
    birth_year = db.Column(db.String(100),  unique=True, nullable=False)
    gender = db.Column(db.String(100),  unique=True, nullable=False)
    
    
    def __repr__(self):
        return '<Person %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height":self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "eye": self.eye,
            "birth_year": self.birth_year,
            "gender": self.gender
            
        }


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    rotation_period = db.Column(db.String(100), unique=True, nullable=False)
    orbital_period = db.Column(db.String(100), unique=True, nullable=False)
    diameter = db.Column(db.String(100), unique=True, nullable=False)
    climate = db.Column(db.String(100), unique=True, nullable=False)
    gravity = db.Column(db.String(100), unique=True, nullable=False) 
    terrain = db.Column(db.String(100), unique=True, nullable=False)
    surface_water = db.Column(db.String(100), unique=True, nullable=False)
    population = db.Column(db.String(100), unique=True, nullable=False)
   
    def __repr__(self):
        return '<Planet %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "rotation_period":self.rotation_period,
            "orbital_period": self.orbital_period,
            "diameter": self.diameter,
            "climate": self.climate,
            "gravity": self.gravity,
            "terrain": self.terrain,
            "surface_water": self.surface_water,
            "population": self.population,
        }

