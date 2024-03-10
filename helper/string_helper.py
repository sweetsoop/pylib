import json
import re


class StringHelper:
    @staticmethod
    def find_number(source:str, suffix:str) -> float:
        return re.match(r'\d+(?=㎡)')
    
    @staticmethod
    def toJson(source:any) -> str:
        return json.dumps(source, ensure_ascii=False)
