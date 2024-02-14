import re
import requests
from bs4 import BeautifulSoup, Tag


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
        return int(re.sub(r'[^0-9]', '', BS.text(source)))
    
    @staticmethod
    def clean_text(source:str|Tag) -> str:
        source = BS.text(source)
        return source.strip().replace('  ', ' ').removeprefix('[').removesuffix(']')
    
    @staticmethod
    def texts(source:str|Tag, separate:str|None = None) -> list:
        source = source.text if type(source) is Tag else source
        if separate is not None:
            elements = source.split(separate)
        for x in range(len(elements)):
            elements[x] = BS.clean_text(elements[x])
        return elements
        