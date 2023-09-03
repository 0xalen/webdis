import json

import requests as req
import logging

from typing import Optional
from app.common.logging import logger


class ApiService:
    """Generic Service for interacting with API REST services"""

    def __init__(self, base_url, username: str = None, password: str = None, token: str = None):
        self._base_url = base_url
        self._username = username
        self._password = password
        self._token = token

    @property
    def base_url(self):
        return self._base_url

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    @property
    def token(self):
        return self._token

    def get(self, endpoint_address: str, params: dict):
        try:
            base_url = self.base_url
            params.update({
                'token': self.token,
            })
            url = f"{base_url}/{endpoint_address}"

            if self.username and self.password:
                response = req.get(
                    url=url,
                    params=params,
                    auth=(
                        self.username,
                        self.password
                    )
                )
            else:
                response = req.get(
                    url=url,
                    params=params,
                )
        except Exception as e:
            logger.error(f"Error sending GET request: {e}")
        else:
            return response

    def post(self, endpoint_address: str, data: Optional[dict] = None, verify: Optional[bool] = True):
        try:
            base_url = self.base_url
            data.update({
                "token": self.token,
            })
            url = f"{base_url}/{endpoint_address}"

            with req.Session() as session:
                if self.username and self.password:
                    session.auth = (
                        self.username,
                        self.password
                    )
                session.verify = verify

                response = session.post(
                        url=url,
                        json=data
                )
        except Exception as e:
            logger.error(f"Error sending POST request: {e}")
        else:
            return response

    def delete(self, endpoint_address: str, params: dict):
        try:
            base_url = self.base_url
            params.update({
                'token': self.token,
            })
            url = f"{base_url}/{endpoint_address}"

            if self.username and self.password:
                response = req.delete(
                    url=url,
                    params=params,
                    auth=(
                        self.username,
                        self.password
                    )
                )
            else:
                response = req.delete(
                    url=url,
                    params=params,
                )
        except Exception as e:
            logger.error(f"Error sending DELETE request: {e}")
        else:
            return response
