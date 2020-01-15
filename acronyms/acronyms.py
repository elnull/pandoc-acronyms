# A dictionary-like class that manages sets of acronyms.

class Acronyms:
    """A dictionary-like class that manages sets of acronyms."""
    def __init__(self):
        self._values = {}

    @property
    def values(self):
        return self._values
    
    def set(self, acronym):
        self._values[acronym.key] = acronym

    def get(self, key):
        value = self._values.get(key)
        return value
