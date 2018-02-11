from aeroexpress import utils
from .session import Session
from datetime import datetime
from .wrapper.types import Lang
from .wrapper import Version, FreeSeats2


class API(object):
    def __init__(self, url: str, key_file: str=None, cert: str=None, password: str=None):
        self.__session = Session(url, key_file, cert, password)

    def get_version_info(self):
        response = self.__session.make_api_request('getVersionInfo')
        return Version(response)

    def get_free_seats_2(self, menu_id: int, date: datetime, language: Lang, guid: str=None):
        response = self.__session.make_api_request('getFreeSeats2', menuId=menu_id, date=utils.set_datetime(date),
                                                   Guid=guid)
        return FreeSeats2(response)