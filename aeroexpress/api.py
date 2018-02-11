import json
from .session import Session
from .wrapper import Version


class API(object):
    def __init__(self, url: str, key_file: str=None, cert: str=None, password: str=None):
        self.__session = Session(url, key_file, cert, password)

    def get_version_info(self):
        response = self.__session.make_api_request('getVersionInfo')
        return Version(response)
