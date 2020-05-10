from enum import Enum

popupPlace=(330, 250)

class SearchPattern(Enum):
    LOCATION = 1
    PARTNO = 2
    UNDEFINED = 3

class shouldUpdateOrInsert(Enum):
    INSERT = 1
    UPDATE = 2
