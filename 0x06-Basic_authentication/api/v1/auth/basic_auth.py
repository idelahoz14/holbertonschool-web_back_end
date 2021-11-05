#!/usr/bin/env python3
""" Auth module for the API
"""
from flask import Flask, jsonify, abort, request
from api.v1.auth.auth import Auth

class BasicAuth(Auth):
    pass
