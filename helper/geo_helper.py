import requests
from urllib import parse


class GeoHelper:
    @staticmethod
    def get_info_by_naver(address:str, key:str, keyId:str) -> dict:
        address = parse.quote_plus(address)
        headers = {'X-NCP-APIGW-API-KEY-ID': keyId, 'X-NCP-APIGW-API-KEY': key}
        response = requests.get(f'https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?query={address}', headers=headers)
        return response.json()