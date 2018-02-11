class Version(object):
    def __init__(self, json):
        self.__json = json
        self.version = json.get('version')
        self.features = json.get('features')

    @property
    def json(self):
        return self.__json
