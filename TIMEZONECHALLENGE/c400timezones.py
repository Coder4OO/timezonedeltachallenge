#Time zone challenge by Coder400
#Task: Calculate time difference between two dates and timezones.
#Time library is banned in this challenge >:)
import json

class Timezone():
    def __init__(self, name, abreviation, offset, isdst, description, utc):
        self.name = name
        self.abreviation = abreviation
        self.offset = offset
        self.isdst = isdst
        self.description = description
        self.utc = utc
    
def convert_timezone_db(db):
    data = json.load(open(db))
    timezones = []
    for entry in data:
        name = entry['value']
        abbr = entry['abbr']
        offset = entry['offset']
        isdst = entry['isdst']
        desc = entry['text']
        utc = entry['utc']
        timezone = Timezone(name, abbr, offset, isdst, desc, utc)
        timezones.append(timezone)
    return timezones

def retrieve_timezone_by_name(name, file):
    data = convert_timezone_db(file)
    found_timezone = None
    for timezone in data:
        if name.lower() == timezone.name.lower():
            found_timezone = timezone
            break
    return found_timezone