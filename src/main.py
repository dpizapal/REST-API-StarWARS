"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Planet, Person
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)



# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    try:
        users = [user.serialize() for user in User.query.all()]
        return jsonify(users)
    except:
        raise APIException('No users in Database', 404)

# GET user favorites
@app.route('/users/<int:user_id>/favorites', methods=['GET'])
def get_user_favourites(user_id):
    user = User.query.get(user_id)
    if not user:
        raise APIException('No match')
    else:
        favorites = [item.serialize() for item in user.peopleFavourites + user.planetFavourites]
        return jsonify(favorites) 



# GET all characters
@app.route('/characters', methods=['GET'])
def get_all_characters():
    try:
        resp = [character.serialize() for character in Person.query.all()]
        return jsonify(resp)
    except:
        raise APIException('No characters in Database', 404)

# GET single character
@app.route('/characters/<int:character_id>', methods=['GET'])
def get_character(character_id):
    try:
        resp = Person.query.get(character_id)
        return jsonify(resp.serialize())
    except:
        raise APIException('Character not found', 404)

# POST favorite character
@app.route('/favourite/character/<int:character_id>', methods=['POST'])
def add_favourite_character(character_id):
    requestBody = request.json.get("User")                     
    user = User.query.get(requestBody['id'])
    character = Person.query.get(character_id)

    if not user or not character:
        raise APIException('User or character not found')
    elif character in user.peopleFavourites:
        raise APIException('Character already in favorites', 400)
    else:
        user.peopleFavourites.append(character)
        db.session.commit()
        return jsonify(f'{character} added', 200)

# DELETE favorite character
@app.route('/favourite/character/<int:character_id>', methods=['DELETE'])
def delete_favourite_character(character_id):
    request_body = request.json.get("User")                     
    user = User.query.get(request_body['id'])
    character = Person.query.get(character_id)

    if not user or not character:
        raise APIException('User or person not found', 404)
    elif character not in user.peopleFavourites:
        raise APIException(f'{character} is not in favorites', 404)
    else:
        user.peopleFavourites.remove(character)
        db.session.commit()
        return jsonify(f'{character} removed from favorites', 200)



# GET all planets
@app.route('/planets', methods=['GET'])
def get_planets():
    try:
        resp = [x.serialize() for x in Planet.query.all()]
        return jsonify(resp)
    except:
        raise APIException('There are no planets in the Database', 404)

# GET single planet
@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):
    try:
        resp = Planet.query.get(planet_id)
        return jsonify(resp.serialize())
    except:
        raise APIException('Planet not found', 404)

# POST favorite planet
@app.route('/favourite/planet/<int:planet_id>', methods=['POST'])
def add_favourite_planet(planet_id):
    requestBody = request.json.get("User")                     
    user = User.query.get(requestBody['id'])
    planet = Planet.query.get(planet_id)

    if not user or not planet:
        raise APIException('User or planet not found')
    elif planet in user.planetFavourites:
        raise APIException('Planet already in favorites', 400)
    else:
        user.planetFavourites.append(planet)
        db.session.commit()
        return jsonify(f'{planet} added', 200)

# DELETE favorite planet
@app.route('/favourite/planet/<int:planet_id>', methods=['DELETE'])
def delete_favourite_planet(planet_id):
    requestBody = request.json.get("User")                    
    user = User.query.get(requestBody['id'])
    planet = Planet.query.get(planet_id)

    if not user or not planet:
        raise APIException('User or planet not found')
    elif planet not in user.planetFavourites:
        raise APIException('Planet is not in favorites')
    else:
        user.planetFavourites.remove(planet)
        db.session.commit()
        return jsonify(f'{planet} removed from favorites')


# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
