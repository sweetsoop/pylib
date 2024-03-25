import re


class DictUtil:
    @staticmethod
    def clean(source:dict) -> dict:
        ret = {}
        for k, v in source.items():
            if v is not None:
                ret[k] = v
        return ret
            
        