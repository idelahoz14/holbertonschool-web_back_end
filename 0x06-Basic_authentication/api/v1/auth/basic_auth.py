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

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """returns the user email and password from the Base64 decoded value"""
        if not decoded_base64_authorization_header or\
           not isinstance(decoded_base64_authorization_header, str)\
           or ":" not in decoded_base64_authorization_header:
            return (None, None)
        extract = decoded_base64_authorization_header.split(':', 1)
        return (extract[0], extract[1]) if extract else (None, None)

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """returns the User instance based on his email and password"""
        if (
            not user_email or type(user_email) != str
            or not user_pwd or type(user_pwd) != str
        ):
            return None
        try:
            user = User.search({'email': user_email})
        except Exception:
            return None

        if user and user[0].is_valid_password(user_pwd):
            return user[0]
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ overloads Auth and
            retrieves the User instance for a request
        """
        try:
            header = self.authorization_header(request)
            base64_h = self.extract_base64_authorization_header(header)
            decode_h = self.decode_base64_authorization_header(base64_h)
            credents = self.extract_user_credentials(decode_h)
            return self.user_object_from_credentials(credents[0], credents[1])
        except Exception:
            return None
