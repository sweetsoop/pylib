import re


class NumberUtil:
    @staticmethod
    def find_percent(source:str, fallbackValue:int = 0) -> int:
        find = re.search(r'\d+%', source)
        return int(find.group().replace('%','')) if find is not None else fallbackValue
        