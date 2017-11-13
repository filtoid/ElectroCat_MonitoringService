class MonitoringService(object):
    key = None
    type_ = "generic"

    TEMPERATURE = "temperature"
    GENERIC = "generic"
    DOOR = "door"
    MOTION = "motion"

    COLLECTION = [TEMPERATURE, GENERIC, DOOR, MOTION]

    def __init__(self, key=None, type_="generic"):
        self.key = key
        self.type_ = type_

    def set_key(self, key):
        self.key = key

    def set_type(self, type_):
        if not type_ in self.COLLECTION:
            print("Unknown type {}".format(type_))
            self.type_ = self.GENERIC
            return

        self.type = type_

    def  upload_reading():
        # TODO: Call the actual API
    
        pass