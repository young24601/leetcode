"""
Kevin's Robinhood interview question
"""

# log parser
# log levels ALL < DEBUG < INFO < WARN < ERROR < FATAL < OFF
# [timestamp: level]: message
# [2019-05-31 04:09:41,521:GMT+8 INFO]: Parsing article error: Error while fetching url: https://nbonews.com/as-goldman-sachs/ | 403, message='Forbidden'
# filter out logs below/above/equal to a level, or only processing certain entries
# counting logs of a given level
# support addition of stateless/stateful functions and easily change how file is read in
# or how entries are processed

from enum import Enum
import re
import operator

class LogLevels(Enum):
    OFF = 60
    FATAL = 50
    ERROR = 40
    WARN = 30
    INFO = 20
    DEBUG = 10
    ALL = 0

class LogParser:
    def __init__(self):
        self.log_entries = {}
        for item in LogLevels:
            self.log_entries[item.name] = []

    def get_log_file(self):
        print("get_file")

    def process_log_entry(self, log_line, timestamp_format):
        spl = re.match(r"\[(?P<timestamp>" + timestamp_format + ")(?P<level>\w+?)\]: (?P<message>.+)", log_line)
        self.log_entries[spl.group('level')].append({"timestamp": spl.group('timestamp'), "message": spl.group('message')})

    def get_log_entries(self, level, level_operator):
        result = []
        for lev in LogLevels:
            if level_operator(lev.value, LogLevels[level].value):
                result.extend(self.log_entries[lev.name])
        return result

    def get_level_count(self, level):
        try:
            return len(self.log_entries[level])
        except KeyError:
            print("level not found")
            return 0

s1 = "[2019-05-31 04:09:41,521:GMT+8 INFO]: Parsing article1 error: Error while fetching url: https://nbonews.com/as-goldman-sachs/ | 403, message='Forbidden'"
s2 = "[2019-05-31 04:09:41,521:GMT+8 INFO]: Parsing article2 error: Error while fetching url: https://nbonews.com/as-goldman-sachs/ | 403, message='Forbidden'"
s3 = "[2019-05-31 04:09:41,521:GMT+8 ERROR]: Parsing article3 error: Error while fetching url: https://nbonews.com/as-goldman-sachs/ | 403, message='Forbidden'"
obj = LogParser()
obj.process_log_entry(s1, ".+?")
obj.process_log_entry(s2, ".+?")
obj.process_log_entry(s3, ".+?")
print(obj.get_level_count("INFO"))
print(obj.get_level_count("asdf"))
print(obj.get_log_entries("INFO", operator.gt))
print(obj.get_log_entries("INFO", operator.eq))



#print(obj.get_log_entries("ERROR"))
#print(obj.get_log_entries("INFO"))

obj2 = LogParser()
obj2.process_log_entry(s1, ".+?")
#print(obj2.log_entries)
