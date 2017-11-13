import httplib2, urllib
from datetime import datetime
import json 

class MonitoringService(object):
    key = None
    type_ = "generic"
    http = None

    TEMPERATURE = "temperature"
    GENERIC = "generic"
    DOOR = "door"
    MOTION = "motion"

    COLLECTION = [TEMPERATURE, GENERIC, DOOR, MOTION]

    def __init__(self, key=None, type_="generic"):
        self.key = key

        if type_ in self.COLLECTION:
            print("Unknown type {}".format(type_))
            self.type_ = self.GENERIC
            return

        self.type_ = type_
        self.http = httplib2.Http()

    def set_key(self, key):
        self.key = key

    def set_type(self, type_):
        if not type_ in self.COLLECTION:
            print("Unknown type {}".format(type_))
            self.type_ = self.GENERIC
            return

        self.type = type_

    def  upload_reading(self, reading):
        if reading is None or reading == "":
            print("Reading cannot be blank")
            return

        if self.key is None or self.key == "":
            print("Key is not set")
            return

        headers={'X-Api-Key': self.key,'Content-type': 'application/json'}
        time_out = '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.now())
        reading={'reading': reading,'time':str(time_out)}
        body={'reading':reading}
        self.http.request('https://electrocatstudios.com/api/reading', 
                       method="POST", 
                       headers=headers,
                       body=json.dumps(body) )[1]
