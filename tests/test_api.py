import json
import mock
import unittest

from aeroexpress import API


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

    @mock.patch('zeep.Client', MockRequest)
    def test_get_version(self):
        version = self.api.get_version_info()

        self.assertEqual(version.version, 12)
        self.assertEqual(version.features, 'core agent-core schedule3')
