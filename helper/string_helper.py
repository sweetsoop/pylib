import json
import re


class StringHelper:
    @staticmethod
    def find_number(source:str, suffix:str) -> float:
        return re.match(r'\d+(?=㎡)')
    
    @staticmethod
    def to_json(source:any) -> str:
        return json.dumps(source, ensure_ascii=False)
    
    @staticmethod
    def from_json(source:str) -> any:
        return json.loads(source)
