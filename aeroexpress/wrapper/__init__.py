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


class ScheduleBranch(Wrapper):
    def __init__(self, json):
        super(ScheduleBranch, self).__init__(json)

        self.id = json.get('branch.id"')
        self.name = json.get('branch.name')
        self.city = json.get('branch.city')
        self.stations = json.get('branch.stations')


class ScheduleStation(Wrapper):
    def __init__(self, json):
        super(ScheduleStation, self).__init__(json)

        self.id = json.get('station.stationId')
        self.name = json.get('station.stationName')


class ScheduleRoute(Wrapper):
    def __init__(self, json):
        super(ScheduleRoute, self).__init__(json)

        self.route = json.get('route')
        self.first_station = json.get('route.firstStation')
        self.last_station = json.get('route.lastStation')


class ScheduleTrain(Wrapper):
    def __init__(self, json):
        super(ScheduleTrain, self).__init__(json)

        self.train = json.get('train')
        self.num = json.get('train.num')
        self.description = json.get('train.description')
        self.day_num = json.get('train.dayNum')
        self.week_days = json.get('train.weekDays')
        self.stop = json.get('train.stop')


class ScheduleStop(Wrapper):
    def __init__(self, json):
        super(ScheduleStop, self).__init__(json)

        self.arrival = json.get('stop.arrival')
        self.departure = json.get('stop.departure')


class ScheduleItem(Wrapper):
    def __init__(self, json):
        super(ScheduleItem, self).__init__(json)

        self.branch_id = json.get('branch.id')
        self.branch_name = json.get('branch.name')
        self.branch_city = json.get('branch.city')
        self.branch_stations = json.get('branch.stations')
        self.station_id = json.get('station.stationId')
        self.station_name = json.get('station.stationName')
        self.route = json.get('route')
        self.route_first_station = json.get('route.firstStation')
        self.route_last_station = json.get('route.lastStation')
        self.train = json.get('train')
        self.train_num = json.get('train.num')
        self.train_description = json.get('train.description')
        self.train_day_num = json.get('train.dayNum')
        self.train_week_days = json.get('train.weekDays')
        self.train_stop = json.get('train.stop')
        self.stop_station = json.get('stop.station')
        self.stop_arrival = json.get('stop.arrival')
        self.stop_departure = json.get('stop.departure')


class Schedule(Wrapper):
    def __init__(self, json):
        super(Schedule, self).__init__(json)

        self.items = utils.get_array(json.get('item'), ScheduleItem)


class RequestTickets3(Wrapper):
    def __init__(self, json):
        super(RequestTickets3, self).__init__(json)


class OrderTicket(Wrapper):
    def __init__(self, json):
        super(OrderTicket, self).__init__(json)

        self.ticket_id = json.get('ticketId')
        self.st_depart = json.get('stDepart')
        self.st_arrival = json.get('stArrival')
        self.tariff = json.get('tariff')
        self.trip_date = utils.get_datetime(json.get('tripDate'))
        self.trip_time = json.get('tripTime')
        self.valid_until = utils.get_datetime(json.get('validUntil'))
        self.ticket_price = json.get('ticketPrice')
        self.ticket_url = json.get('ticketUrl')
        self.first_name = json.get('firstName')
        self.patronymic_name = json.get('patronymicName')
        self.surname = json.get('surname')
        self.doc_type = json.get('docType')
        self.doc_number = json.get('docNumber')


class OrderTickets(Wrapper):
    def __init__(self, json):
        super(OrderTickets, self).__init__(json)

        self.tickets = [] if type(json.get('tickets')) is not dict else utils.get_array(json['tickets'].get('ticket'), OrderTicket)


class DocumentType(Wrapper):
    def __init__(self, json):
        super(DocumentType, self).__init__(json)

        self.doc_type_id = json.get('docTypeId')
        self.doc_type_name = json.get('docTypeName')
        self.input_mask = json.get('inputMask')


class DocumentTypeResponse(Wrapper):
    def __init__(self, json):
        super(DocumentTypeResponse, self).__init__(json)

        self.documents = [] if type(json.get('documentTypes')) is not dict else utils.get_array(json['documentTypes'].get('documentType'), DocumentType)

