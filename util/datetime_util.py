from datetime import datetime


class DateTimeUtil:
    @staticmethod
    def to_date(source:str, isLast:bool = False) -> datetime:
        ret = datetime.strptime(source, '%Y-%m-%d')
        return ret if isLast == False else datetime(ret.year, ret.month, ret.day, 23, 59, 59)
    
    def range_datetime(base:datetime) -> tuple[datetime, datetime]:
        return (datetime(base.year, base.month, base.day), datetime(base.year, base.month, base.day, 23, 59, 59))