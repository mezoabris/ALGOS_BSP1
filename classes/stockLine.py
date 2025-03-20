import json
from json import JSONEncoder

class stockLine:
     def __init__(self, date, closeLast,volume, open, high, low):
        self.date = date
        self.closeLast = closeLast
        self.volume = volume
        self.open = open
        self.high = high
        self.low = low

class EncodeList(JSONEncoder):
      def default(self, o):
          return o.__dict__
