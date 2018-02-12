from aeroexpress import utils
from .session import Session
from datetime import datetime
from .wrapper.types import Lang
from .wrapper import Version, FreeSeats2, OrderContacts, WwwMenu, RequestTickets2, PayOrder


class API(object):
    def __init__(self, url: str, key_file: str=None, cert: str=None, password: str=None):
        self.__session = Session(url, key_file, cert, password)

    def get_version_info(self):
        response = self.__session.make_api_request('getVersionInfo')
        return Version(response)

    def get_free_seats_2(self, menu_id: int, date: datetime, language: Lang=Lang.RUSSIAN, guid: str=None):
        response = self.__session.make_api_request('getFreeSeats2', menuId=menu_id, date=utils.set_datetime(date),
                                                   Guid=guid, language=language)
        return FreeSeats2(response)

    def set_order_contacts(self, order_id: int, language: Lang=Lang.RUSSIAN, email: str=None, phone: str=None):
        response = self.__session.make_api_request('setOrderContacts', orderId=order_id, language=language,
                                                   email=email, phone=phone)
        # test server
        return OrderContacts(response)

    def get_www_menu(self, menu_id: int, language: Lang=Lang.RUSSIAN, guid: str=None):
        response = self.__session.make_api_request('getWwwMenu', menuId=menu_id, Guid=guid, language=language)
        return WwwMenu(response)

    def request_tickets_2(self, menu_id: int, departure_date: datetime, order_type: int, guid: str=None):
        response = self.__session.make_api_request('requestTickets2', menuId=menu_id,
                                                   departDate=utils.set_datetime(departure_date),
                                                   Guid=guid, orderType=order_type)
        return RequestTickets2(response)

    def pay_order(self, order_id: int, language: Lang=Lang.RUSSIAN):
        response = self.__session.make_api_request('payOrder', OrderId=order_id, language=language)
        return PayOrder(response)

