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

