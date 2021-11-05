#!/usr/bin/env python3
""" Auth module for the API
"""
from flask import Flask, request
from typing import List, TypeVar


class Auth:
    """ Class to manage the API authentication.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Require authorithation check
        """
        if path is None or excluded_paths is None or not len(excluded_paths):
            return True
        if path[-1] != '/':
            path += '/'
        return False if path in excluded_paths else True

    def authorization_header(self, request=None) -> str:
        """ Authorithation header check
        """
        if request is None:
            return None

        if request:
            request.header.get('Authorithation')

    def current_user(self, request=None) -> TypeVar('User'):
        """ Current user check
        """
        return None
