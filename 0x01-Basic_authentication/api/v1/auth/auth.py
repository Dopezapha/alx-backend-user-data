#!/usr/bin/env python3
"""
Module of Auth views
"""
from flask import request
from typing import List, Optional


class Auth:
    """
    manage the API authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Check if authentication is required for the given path.
        """
        if not path:
            return True

        # Ensure path ends with '/'
        path = path.rstrip('/') + '/'

        if not excluded_paths:
            return True

        return path not in [p.rstrip('/') + '/' for p in excluded_paths]

    def authorization_header(self, request=None) -> Optional[str]:
        """
        Check the authorization header
        """
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> None:
        """
        Check the current user
        """
        return None


if __name__ == "__main__":
    a = Auth()

    print(a.require_auth(None, None))  # True
    print(a.require_auth(None, []))  # True
    print(a.require_auth("/api/v1/status/", []))  # True
    print(a.require_auth("/api/v1/status/", ["/api/v1/status/"]))  # False
    print(a.require_auth("/api/v1/status", ["/api/v1/status/"]))  # False
    print(a.require_auth("/api/v1/users", ["/api/v1/status/"]))  # True
    print(a.require_auth("/api/v1/users", ["/api/v1/status/",
                                           "/api/v1/stats"]))  # True
