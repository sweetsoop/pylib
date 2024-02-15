from configparser import ConfigParser


class ConfigLoader:
    def __init__(self, path:str, defaultGroup:str = 'common') -> None:
        self.configParser = ConfigParser()
        self.configParser.read(path)
        self.defaultGroup = defaultGroup

    def get(self, group:str, key:str) -> str:
        group = group if len(group) > 0 else 'common'
        return self.configParser[group][key]
    