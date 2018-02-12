import json
import mock
import unittest
from aeroexpress import API
from datetime import datetime
from aeroexpress.wrapper.types import Lang, Day
from aeroexpress.wrapper.request import PersonalInfo


class JsonLoader(object):
    def __init__(self, method):
        self.method = method

    def __json__(self):
        return json.loads(open('tests/data/%s.json' % self.method, 'r', encoding='utf8').read())


class MockService(object):
    def __init__(self):
        self.method = None

    def __getattr__(self, item):
        self.method = item
        return self.get_data

    def get_data(self, **kwargs):
        return JsonLoader(self.method)


class MockRequest(object):
    def __init__(self, param1, param2):
        self.service = MockService()


class TestAPI(unittest.TestCase):

    @mock.patch('zeep.Client', MockRequest)
    def setUp(self):
        self.maxDiff = None
        self.api = API('url')
        self.datetime = datetime.fromtimestamp(0).replace(hour=3)

    @mock.patch('zeep.Client', MockRequest)
    def test_get_version(self):
        version = self.api.get_version_info()

        self.assertEqual(version.version, 12)
        self.assertEqual(version.features, 'core agent-core schedule3')

    def test_get_free_seats_2(self):
        trips = self.api.get_free_seats_2(0, self.datetime, Lang.RUSSIAN)

        self.assertEqual(trips.trips[0].trip, "00:00-00:30")
        self.assertEqual(trips.trips[0].date, self.datetime)
        self.assertEqual(trips.trips[0].seats, 20)
        self.assertEqual(trips.trips[0].sched_id, 123)

    def test_set_order_contacts(self):
        order_contacts = self.api.set_order_contacts(1, Lang.RUSSIAN, 'tt@tt.tt')

        self.assertEqual(order_contacts.json, {})

    def test_www_menu(self):
        www_menu = self.api.get_www_menu(1, Lang.RUSSIAN)

        self.assertEqual(www_menu.items[0].id, 1)
        self.assertEqual(www_menu.items[0].name, 'name')
        self.assertEqual(www_menu.items[0].last_id, False)
        self.assertEqual(www_menu.items[0].price, 1)
        self.assertEqual(www_menu.items[0].order_type, 1)
        self.assertEqual(www_menu.items[0].max_tickets, 1)
        self.assertEqual(www_menu.items[0].max_days, 1)
        self.assertEqual(www_menu.items[0].description, 'description')

        self.assertEqual(www_menu.items[0].items[0].id, 2)
        self.assertEqual(www_menu.items[0].items[0].name, 'name2')
        self.assertEqual(www_menu.items[0].items[0].last_id, True)
        self.assertEqual(www_menu.items[0].items[0].price, 2)
        self.assertEqual(www_menu.items[0].items[0].order_type, 2)
        self.assertEqual(www_menu.items[0].items[0].max_tickets, 2)
        self.assertEqual(www_menu.items[0].items[0].max_days, 2)
        self.assertEqual(www_menu.items[0].items[0].description, 'description2')

    def test_request_tickets_2(self):
        request_tickets = self.api.request_tickets_2(1, self.datetime, 1)

        self.assertEqual(request_tickets.order_id, 1)
        self.assertEqual(request_tickets.sum, 1)
        self.assertEqual(request_tickets.details, 'details')
        self.assertEqual(request_tickets.hash, 'hash')
        self.assertEqual(request_tickets.status_url, 'status_url')

    def test_pay_order(self):
        pay_order = self.api.pay_order(1)

        self.assertEqual(pay_order.items[0].code, "code")
        self.assertEqual(pay_order.items[0].ticket_id, 1)
        self.assertEqual(pay_order.items[0].ticket_guid, "ticket_guid")
        self.assertEqual(pay_order.items[0].ticket_url, "ticket_url")
        self.assertEqual(pay_order.items[0].token, "token")
        self.assertEqual(pay_order.items[0].trip_date, self.datetime)
        self.assertEqual(pay_order.items[0].trip_time, "00:00")
        self.assertEqual(pay_order.items[0].st_arrival, "st_arrival")
        self.assertEqual(pay_order.items[0].st_depart, "st_depart")
        self.assertEqual(pay_order.items[0].tariff, "tariff")
        self.assertEqual(pay_order.items[0].ticket_price, "ticket_price")

    def test_cancel_order(self):
        cancel_order = self.api.cancel_order(1)

        self.assertEqual(cancel_order.json, {})

    def test_get_schedule_4(self):
        schedule = self.api.get_schedule_4()

        self.assertEqual(schedule.items[0].branch_id, 1)
        self.assertEqual(schedule.items[0].branch_name, 'branch_name')
        self.assertEqual(schedule.items[0].branch_city, 'branch_city')
        self.assertEqual(schedule.items[0].branch_stations, 'branch_stations')
        self.assertEqual(schedule.items[0].station_id, 1)
        self.assertEqual(schedule.items[0].station_name, 'station_name')
        self.assertEqual(schedule.items[0].route, 'route')
        self.assertEqual(schedule.items[0].route_first_station, 'first_station')
        self.assertEqual(schedule.items[0].route_last_station, 'last_station')
        self.assertEqual(schedule.items[0].train, None)
        self.assertEqual(schedule.items[0].train_num, 1)
        self.assertEqual(schedule.items[0].train_description, 'train_description')
        self.assertEqual(schedule.items[0].train_day_num, Day.EVEN)
        self.assertEqual(schedule.items[0].train_week_days, None)
        self.assertEqual(schedule.items[0].train_stop, None)
        self.assertEqual(schedule.items[0].stop_station, 1)
        self.assertEqual(schedule.items[0].stop_arrival, '00:00')
        self.assertEqual(schedule.items[0].stop_departure, '00:00')

    def test_request_tickets_3(self):
        request_tickets = self.api.request_tickets_3([PersonalInfo('', '', '', '', '')], None)

        self.assertEqual(request_tickets.json, {})

    def test_get_order_tickets(self):
        order_tickets = self.api.get_order_tickets(1)

        self.assertEqual(order_tickets.tickets[0].ticket_id, 0)
        self.assertEqual(order_tickets.tickets[0].st_depart, '')
        self.assertEqual(order_tickets.tickets[0].st_arrival, '')
        self.assertEqual(order_tickets.tickets[0].tariff, '')
        self.assertEqual(order_tickets.tickets[0].trip_date, self.datetime)
        self.assertEqual(order_tickets.tickets[0].trip_time, '00:00')
        self.assertEqual(order_tickets.tickets[0].valid_until, self.datetime)
        self.assertEqual(order_tickets.tickets[0].ticket_price, 400)
        self.assertEqual(order_tickets.tickets[0].ticket_url, '')
        self.assertEqual(order_tickets.tickets[0].first_name, 'first_name')
        self.assertEqual(order_tickets.tickets[0].patronymic_name, 'patronymic_name')
        self.assertEqual(order_tickets.tickets[0].surname, 'surname')
        self.assertEqual(order_tickets.tickets[0].doc_type, 'doc_type')
        self.assertEqual(order_tickets.tickets[0].doc_number, 'doc_number')
