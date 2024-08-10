#!/usr/bin/python3
"""Routes for State objects"""

from flask import jsonify, request
from api.v1.views import app_views
from models import storage
from models.state import State

@app_views.route('/states', methods=['GET'])
def get_states():
    """Retrieve all State objects"""
    states = storage.all(State).values()
    return jsonify([state.to_dict() for state in states])

@app_views.route('/states/<state_id>', methods=['GET'])
def get_state(state_id):
    """Retrieve a State object by ID"""
    state = storage.get(State, state_id)
    if state is None:
        return jsonify(error="Not found"), 404
    return jsonify(state.to_dict())

@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    """Delete a State object by ID"""
    state = storage.get(State, state_id)
    if state is None:
        return jsonify(error="Not found"), 404
    storage.delete(state)
    storage.save()
    return jsonify({})

@app_views.route('/states', methods=['POST'])
def create_state():
    """Create a new State object"""
    if not request.is_json:
        return jsonify(error="Not a JSON"), 400
    data = request.get_json()
    if 'name' not in data:
        return jsonify(error="Missing name"), 400
    state = State(**data)
    state.save()
    return jsonify(state.to_dict()), 201

@app_views.route('/states/<state_id>', methods=['PUT'])
def update_state(state_id):
    """Update a State object by ID"""
    if not request.is_json:
        return jsonify(error="Not a JSON"), 400
    data = request.get_json()
    state = storage.get(State, state_id)
    if state is None:
        return jsonify(error="Not found"), 404
    for key, value in data.items():
        if key not in ["id", "created_at", "updated_at"]:
            setattr(state, key, value)
    state.save()
    return jsonify(state.to_dict())
