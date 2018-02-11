from aeroexpress import utils
from .session import Session
from datetime import datetime
from .wrapper.types import Lang
from .wrapper import Version, FreeSeats2, OrderContacts, WwwMenu


class API(object):
    def __init__(self, url: str, key_file: str=None, cert: str=None, password: str=None):
        self.__session = Session(url, key_file, cert, password)

    def get_version_info(self):
        response = self.__session.make_api_request('getVersionInfo')
        return Version(response)

    def get_free_seats_2(self, menu_id: int, date: datetime, language: Lang, guid: str=None):
        response = self.__session.make_api_request('getFreeSeats2', menuId=menu_id, date=utils.set_datetime(date),
                                                   Guid=guid, language=language)
        return FreeSeats2(response)

    def set_order_contacts(self, order_id: int, language: Lang, email: str=None, phone: str=None):
        response = self.__session.make_api_request('setOrderContacts', orderId=order_id, language=language,
                                                   email=email, phone=phone)
        # test server
        return OrderContacts(response)

    def get_www_menu(self, menu_id: int, language: Lang, guid: str=None):
        response = self.__session.make_api_request('getWwwMenu', menuId=menu_id, Guid=guid, language=language)
        return WwwMenu(response)