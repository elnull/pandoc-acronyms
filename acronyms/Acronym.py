# A class that represents one acronym.

class Acronym:
    def __init__(self, _key = "", _shortform = "", _longform = ""):
        self.key = _key
        self.shortform = _shortform
        self.longform = _longform

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, key):
        self._key = str(key)
