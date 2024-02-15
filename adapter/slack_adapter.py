import requests


class SlackAdapter:
    def __init__(self, webHook:str) -> None:
        self.__webHook = webHook

    def send_message(self, message:str) -> bool:
        response = requests.post(self.__webHook, json = {'text': message})
        return True if response.status_code == 200 else False