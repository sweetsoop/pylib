import re
import requests
from bs4 import BeautifulSoup, Tag
from datetime import datetime


class BS:
    @staticmethod
    def request(host:str, header:object = None, data:object = None, encoding:str = 'utf-8', features:str = 'lxml') -> BeautifulSoup:
        response = requests.post(host, headers=header, data=data)
        return BeautifulSoup(response.content.decode(encoding), features)
    
    @staticmethod
    def text(source:str|Tag) -> str:
        return source if type(source) is str else source.text
    
    @staticmethod
    def int(source:str|Tag) -> int:
        source = BS.clean_text(source)
        if (source == ''):
            return 0
        return int(re.sub(r'[^0-9]', '', BS.clean_text(source)))
    
    @staticmethod
    def datetime(source:str|Tag, pattern:str) -> datetime:
        source = BS.clean_text(source)
        return datetime.strptime(source, pattern)
        
    @staticmethod
    def remove_number(source:str|Tag) -> str:
        return BS.clean_text(re.sub(r'\d+', '', BS.text(source)))
    
    @staticmethod
    def remove_element(source:list, removeElement:str) -> list:
        return list(filter(lambda str: str != removeElement, source))
    
    @staticmethod
    def single_quote_list(source:str) -> list:
        return re.compile("(?<=')[^']+(?=')").findall(source)
    
    @staticmethod
    def clean_text(source:str|Tag) -> str:
        source = BS.text(source)
        return source.strip().replace('  ', ' ').removeprefix('[').removesuffix(']')
    
    @staticmethod
    def clean_texts(source:list) -> None:
        for x in range(len(source)):
            source[x] = BS.clean_text(source[x])
    
    @staticmethod
    def texts(source:str|Tag, separate:str|None = None) -> list:
        source = BS.text(source)
        if separate is not None:
            elements = source.split(separate)
        BS.clean_texts(elements)
        return BS.arrange_list(elements)
    
    @staticmethod
    def numbers(source:str|Tag, separate:str|None = None) -> list:
        source = BS.text(source)
        if separate is not None:
            elements = source.split(separate)
        BS.clean_texts(elements)
        newList = BS.arrange_list(elements)
        for x in range(len(newList)):
            newList[x] = BS.int(newList[x])
        return newList
        
    @staticmethod
    def arrange_list(source:list, removeTag:bool = False) -> list:
        newList = list(filter(None, source))
        if removeTag:
            newList = list(filter(lambda str: type(str) is not Tag, newList))
            BS.clean_texts(newList)
        return newList