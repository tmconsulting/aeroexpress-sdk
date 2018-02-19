import zeep
import logging
import requests
from zeep.wsse import Signature
from zeep.transports import Transport

logger = logging.getLogger('Session')


class Session(object):
    def __init__(self, url, key_file=None, cert=None, password=None):

        self.last_response_data = None
        self.last_request_data = None

        self.url = url

        self.session = requests.Session()
        self.session.cert = (cert, key_file)
        self.session.verify = False

        self.transport = Transport(session=self.session)
        self.wsse = Signature(key_file, cert, password) if key_file is not None else None
        self.client = zeep.Client(self.url, self.wsse, self.transport)

    def make_api_request(self, method, **data):
        try:
            response = self.__send_api_request(method, **data)
            response = response.__json__()
        except:
            # test server
            logger.exception('make_api_request')
            return {}
        self.last_response_data = response
        return response

    def __send_api_request(self, method, **data):
        return self.client.service.__getattr__(method)(**data)
