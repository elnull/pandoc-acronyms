# A dictionary-like class that manages sets of acronyms.
from acronyms.json_codec import AcronymJSONEncoder
from acronyms.acronym import Acronym
import json

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

    @staticmethod
    def Read(fileobject):
        """Read() generates an Acronyms object from the JSON data and returns it."""
        data = json.load(fileobject)
        acronyms = Acronyms()
        for key, value in data.items():
            acronym = Acronym()
            acronym.key = key
            acronym.shortform = value['shortform']
            acronym.longform = value['longform']
            acronyms.set(acronym)
        return acronyms

    def write(self, fileobject):
        data = AcronymJSONEncoder().encode(self.values)
        fileobject.write(data)
