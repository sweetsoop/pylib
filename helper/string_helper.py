import re


class StringHelper:
    @staticmethod
    def find_number(source:str, suffix:str) -> float:
        return re.match(r'\d+(?=㎡)')
