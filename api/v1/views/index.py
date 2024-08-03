#!/usr/bin/python3
""" """

from api.v1.views import app_views
from flask import Flask, jsonify
from models import storage


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    counts = {
        "amenities": storage.count('amenities'),
        "cities": storage.count('cities'),
        "places": storage.count('places'),
        "reviews": storage.count('reviews'),
        "states": storage.count('states'),
        "users": storage.count('users'),
    }
    return jsonify(counts)
