'''
Created on Sep 3, 2014

@author: TuanNA
'''
import datetime
from json import JSONEncoder

class DateEncoder(JSONEncoder):
    def default(self, obj):
        if obj is None:
            return ''
        if isinstance(obj, datetime.date):
            return obj.strftime('%d/%m/%Y')
        elif isinstance(obj, datetime):
            return obj.date.strftime('%d/%m/%Y')
        return JSONEncoder.default(self, obj)
class DateTimeEncoder(JSONEncoder):
    def default(self, obj):
        if obj is None:
            return ''
        if isinstance(obj, datetime.date):
            return obj.strftime('%d/%m/%Y %H:%M:%S')
        elif isinstance(obj, datetime):
            return obj.date.strftime('%d/%m/%Y %H:%M:%S')
        return JSONEncoder.default(self, obj)