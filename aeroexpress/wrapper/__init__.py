from aeroexpress import utils


class Wrapper(object):
    def __init__(self, json):
        self.__json = json

    @property
    def json(self):
        return self.__json


class Version(Wrapper):
    def __init__(self, json):
        super(Version, self).__init__(json)

        self.version = json.get('version')
        self.features = json.get('features')


class Trip(Wrapper):
    def __init__(self, json):
        super(Trip, self).__init__(json)

        self.trip = json.get('Trip')
        self.date = utils.get_datetime(json.get('Date'))
        self.seats = json.get('Seats')
        self.sched_id = json.get('schedId')


class FreeSeats2(Wrapper):
    def __init__(self, json):
        super(FreeSeats2, self).__init__(json)

        self.trips = utils.get_array(json.get('trips'), Trip)


class OrderContacts(Wrapper):
    def __init__(self, json):
        super(OrderContacts, self).__init__(json)


class WwwMenuItem(Wrapper):
    def __init__(self, json):
        super(WwwMenuItem, self).__init__(json)

        self.id = json.get('Id')
        self.name = json.get('Name')
        self.last_id = utils.get_bool(json.get('lastId'))
        self.price = json.get('Price')
        self.label = json.get('Label')
        self.order_type = json.get('orderType')
        self.max_tickets = json.get('maxTickets')
        self.max_days = json.get('maxDays')
        self.description = json.get('Description')

        self.items = utils.get_array(json.get('item'), WwwMenuItem)


class WwwMenu(Wrapper):
    def __init__(self, json):
        super(WwwMenu, self).__init__(json)
        self.items = utils.get_array(json.get('item'), WwwMenuItem)


class RequestTickets2(Wrapper):
    def __init__(self, json):
        super(RequestTickets2, self).__init__(json)

        self.order_id = json.get('orderId')
        self.sum = json.get('Sum')
        self.details = json.get('Details')
        self.hash = json.get('Hash')
        self.status_url = json.get('statusUrl')


class PayOrderItem(Wrapper):
    def __init__(self, json):
        super(PayOrderItem, self).__init__(json)

        self.code = json.get('Code')
        self.ticket_id = json.get('ticketId')
        self.ticket_guid = json.get('ticketGuid')
        self.ticket_url = json.get('ticketUrl')
        self.token = json.get('Token')
        self.trip_date = utils.get_datetime(json.get('tripDate'))
        self.trip_time = json.get('tripTime')
        self.st_arrival = json.get('stArrival')
        self.st_depart = json.get('stDepart')
        self.tariff = json.get('Tariff')
        self.ticket_price = json.get('ticketPrice')


class PayOrder(Wrapper):
    def __init__(self, json):
        super(PayOrder, self).__init__(json)

        self.items = utils.get_array(json.get('item'), PayOrderItem)


class CancelOrder(Wrapper):
    def __init__(self, json):
        super(CancelOrder, self).__init__(json)
