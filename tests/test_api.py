import json
import mock
import unittest
from aeroexpress import API
from datetime import datetime
from aeroexpress.wrapper.types import Lang


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