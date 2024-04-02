import re


class DictUtil:
    @staticmethod
    def get(key:str, source:dict) -> any:
        return source[key] if source[key] is not None else None

    @staticmethod
    def clean(source:dict) -> dict:
        ret = {}
        for k, v in source.items():
            if v is not None:
                ret[k] = v
        return ret