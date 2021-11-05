#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None


if os.getenv('AUTH_TYPE') == 'auth':
    from api.v1.auth.auth import Auth
    auth = Auth()


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """ Bad authentification
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """ Bad authentification
    """
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def before_reques() -> None:
    """ Filtering of each request
    """
    PATHS = ['/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/']
    if auth is None:
        return None
    if not auth.require_auth(request.path, PATHS):
        return None
    if not auth.authorization_header(request):
        return abort(401)
    if not auth.current_user(request):
        return abort(403)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)