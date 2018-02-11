import zeep
import logging
from zeep.wsse import Signature

logger = logging.getLogger('Session')


class Session(object):
    def __init__(self, url, key_file=None, cert=None, password=None):

        self.last_response_data = None
        self.last_request_data = None

        self.url = url
        self.wsse = Signature(key_file, cert, password) if key_file is not None else None
        self.client = zeep.Client(self.url, self.wsse)

    def make_api_request(self, method, **data):
        try:
            response = self.__send_api_request(method, **data)
            response = response.__json__()
        except:
            # need test server
            logger.exception('make_api_request')
            return {}
        self.last_response_data = response
        return response

    def __send_api_request(self, method, **data):
        return self.client.service.__getattr__(method)(**data)
