import re
import json
from datetime import datetime

class StrHelper:
    @staticmethod
    def find_number(source:str, suffix:str) -> float:
        return re.match(r'\d+(?=㎡)')
    
    @staticmethod
    def to_json(source:any) -> str:
        return json.dumps(source, ensure_ascii=False)
    
    @staticmethod
    def from_json(source:str) -> any:
        return json.loads(source)
    
    @staticmethod
    def datetime(source:datetime) -> str | None:
        return source.strftime('%Y-%m-%d') if source is not None else None
