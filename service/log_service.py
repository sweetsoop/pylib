from datetime import datetime


class Logger:
    instance = None
    messages = []

    def __init__(self) -> None:
        raise RuntimeError('Call to() instead')
    
    @classmethod
    def to(cls):
        if cls.instance is None:
            cls.instance = cls.__new__(cls)
        return cls.instance
    
    def add(self, message:str):
        self.messages.append(message)

    def print(self):
        for message in self.messages:
            print(message)

    def write(self):
        file = open(datetime.now().strftime('%Y%m%d') + '.log', 'w')
        for message in self.messages:
            file.write(message + '\n')
        file.close()