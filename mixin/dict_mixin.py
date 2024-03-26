from datetime import datetime
from pylib.helper.string_helper import StrHelper


class DictMixin:
    def to_dict(self, includeNone:bool = False):
        output = {}
        for k, v in self.__dict__.items():
            if includeNone == False and v is None: continue
            output[k] = self._convert(v)
        return output
    
    def _convert(self, source:any) -> any:
        if isinstance(source, datetime):
            return StrHelper.datetime(source)
        else:
            return source