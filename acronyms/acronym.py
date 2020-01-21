class Acronym:
    """A class that represents one acronym."""
    def __init__(self, _key = '', _shortform = '', _longform = ''):
        self.key = _key
        self.shortform = _shortform
        self.longform = _longform

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, key):
        self._key = str(key)

    @property
    def shortform(self):
        return self._shortform

    @shortform.setter
    def shortform(self, shortform):
        self._shortform = str(shortform)

    @property
    def longform(self):
        return self._longform

    @longform.setter
    def longform(self, longform):
        self._longform = str(longform)

    def __eq__(self, other):
        if not isinstance(other, Acronym):
            return NotImplemented
        return self.key == other.key and self.shortform == other.shortform and self.longform == other.longform
