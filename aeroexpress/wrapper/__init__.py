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
        self.__json = json
        self.version = json.get('version')
        self.features = json.get('features')


class Trip(object):
    def __init__(self, json):
        self.trip = json.get('Trip')
        self.date = utils.get_datetime(json.get('Date'))
        self.seats = utils.get_item(json.get('Seats'), int)
        self.sched_id = utils.get_item(json.get('schedId'), int)


class FreeSeats2(Wrapper):
    def __init__(self, json):
        super(FreeSeats2, self).__init__(json)
        self.__json = json
        self.trips = utils.get_array(json.get('trips'), Trip)


class OrderContacts(Wrapper):
    def __init__(self, json):
        super(OrderContacts, self).__init__(json)
        self.__json = json
