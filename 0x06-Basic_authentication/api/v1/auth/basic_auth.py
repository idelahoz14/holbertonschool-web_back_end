#!/usr/bin/env python3
""" Auth module for the API
"""
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth
from models.user import User
import base64


class BasicAuth(Auth):
    """ Basic Auth class
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """returns the Base64 part
        of the Authorization header for a Basic Authentication"""
        if authorization_header is None or\
           type(authorization_header) is not str:
            return None
        header = authorization_header.split(' ')

        return header[1] if header[0] == 'Basic' else None
