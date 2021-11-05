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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """return the decoded value as UTF8 string
            you can use decode('utf-8')
        """
        if base64_authorization_header is None or\
           type(base64_authorization_header) is not str:
            return None
        try:
            bBytes = base64_authorization_header.encode('utf-8')
            msg_bytes = base64.b64decode(bBytes)
            return msg_bytes.decode('utf-8')
        except Exception:
            return None
