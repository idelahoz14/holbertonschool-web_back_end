from flask import Flask, request


class Auth:
    """
    """

    @property
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        """
        return False

    @property
    def authorization_header(self, request=None) -> str:
        """
        """
        return None

    @property
    def current_user(self, request=None) -> TypeVar('User'):
        """
        """
        return None
