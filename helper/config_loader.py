from configparser import ConfigParser


class ConfigLoader:
    def __init__(self, path:str, defaultGroup:str = 'common') -> None:
        self.configParser = ConfigParser()
        self.configParser.read(path)
        self.defaultGroup = defaultGroup

    def get(self, key:str, group:str|None = None) -> str:
        targetGroup = self.configParser[self.defaultGroup] if group is None else self.configParser[group]
        return targetGroup[key]
    